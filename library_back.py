from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from decimal import Decimal

# create engine and base
engine = create_engine('sqlite:///data.db')
Base = declarative_base()

# main item class
class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True, autoincrement=True)  # main item id, will autoincrement when an item is added
    branch_id = Column(Integer, ForeignKey('branch.branch_id'), nullable=False)  # id of the branch the item is located
    patron_id = Column(Integer, ForeignKey('patron.patron_id'), nullable=True)  # id of patron who currently has item checked out, null when not checked out
    isbn = Column(String(13), ForeignKey('book.isbn'), nullable=True)  # isbn of book, null for movies
    isan = Column(String(22), ForeignKey('movie.isan'), nullable=True)  # isan of movie, null for books
    item_type = Column(String(5), nullable=False)  # the type of item, either book or movie
    status = Column(String(11), nullable=False)  # if the item is checked out, either available or checked out
    title = Column(String(300), nullable=False)  # title of the item
    genre = Column(String(30), nullable=False)  # genre of content
    
    # constraints on data
    __table_args__ = (
        CheckConstraint("item_type IN ('book','movie')"),
        CheckConstraint("status IN ('available','checked out')")
    )
    
    def __repr__(self):
        return f"{self.item_id}, {self.title}"


# book item class
class Book(Base):
    __tablename__ = 'book'
    isbn = Column(String(13), primary_key=True)  # isbn of book, acts as primary key since it is unique
    author_id = Column(Integer, ForeignKey('author.author_id'), nullable=False)  # id of author who wrote the book
    medium = Column(String(11), nullable=False)  # The format the item is in, must be ebook, paperback, hard cover, or large print
    pages = Column(Integer)  # the number of pages in the book

    __table_args__ = (
        (CheckConstraint("medium IN ('ebook','paperback','hard cover','large print')"),)
    )
    
    def __repr__(self):
        return f"{self.isbn}"


# author class
class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True, autoincrement=True)  # pk of author class, will autoincrement
    author_name = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"{self.author_id}, {self.author_name}"


# movie item class
class Movie(Base):
    __tablename__ = 'movie'
    isan = Column(String(22), primary_key=True)  # ISAN of movie, acts as primary key since it is unique
    runtime = Column(Integer, nullable=False)  # runtime of movie in minutes
    medium = Column(String(7), nullable=False)  # format of the item, must be vhs, dvd, or blu-ray 
    
    __table_args__ = (
        (CheckConstraint("medium IN ('vhs','dvd','blu-ray')"),)
    )
    
    def __repr__(self):
        return f"{self.isan}"


# patron class
class Patron(Base):
    __tablename__ = 'patron'
    patron_id = Column(Integer, primary_key=True, autoincrement=True)  # pk of patron class, will autoincrement
    branch_id = Column(Integer, ForeignKey('branch.branch_id'), nullable=False)  # branch _id of their home branch
    patron_name = Column(String(30), nullable=False)  # name of the patron
    phone = Column(String(14), nullable=False)  # contact phone of patron
    account_type = Column(String(5), nullable=False)  # The account type for determining check out limits, must be child or adult
    limit_reached = Column(Boolean, nullable=False, default=False)  # Boolean indicating if the patron is at their check out limit
    fees = Column(Numeric(precision=5, scale=2), nullable=False, default=0.00)  # the amount the patron owes in fees
    
    
    __table_args__ = (
        (CheckConstraint("account_type IN ('Adult','Child')"),)
    )
    def __repr__(self):
        return f"{self.patron_id}, {self.name}"


# branch class
class Branch(Base):
    __tablename__ = 'branch'
    branch_id = Column(Integer, primary_key=True, autoincrement=True)  # pk of branch table, will auto increment
    branch_name = Column(String(30), nullable=False) # name of branch location
    address = Column(String(100), nullable=False)  # address of branch location
    phone = Column(String(14), nullable=False)  # phone number of branch
    
    def __repr__(self):
        return f"{self.branch_id} {self.address} {self.phone}"


Base.metadata.create_all(engine) # initialize database if there isn't one


###### QUERY FUNCTIONS

# search all books based either title, author, genre, isbn, branch, or any combination
def search_books(title=None, author=None, genre=None, isbn=None, branch_id=None):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = (
            session.query(Item.item_id, Item.title, Author.author_name, Book.medium, Book.pages, Branch.branch_name, Item.status)
            .join(Book, Book.isbn == Item.isbn) # joining the book table for medium and pages
            .join(Author, Author.author_id == Book.author_id) # joining the author table for author info
            .join(Branch, Branch.branch_id == Item.branch_id) # joining branch table
            .filter(Item.title.ilike(f'%{title}%') if title else True)  # Case insensitive search, only active is value not None
            .filter(Author.author_name.ilike(f'%{author}%') if author else True)  # Case insensitive search, only active is value not None 
            .filter(Item.isbn == isbn if isbn else True)  # Looks for exact isbn, only active is value not None
            .filter(Item.genre == genre if genre else True)  # looks for exact genre, only active is value not None
            .filter(Item.branch_id == branch_id if branch_id else True)  # looks for exact branch, only active is value not None
            .all()  # Call the method to execute the query
        )
        print(query)
    return query


# same as book search but movies
def search_movies(title=None, genre=None, isan=None, runtime=None, branch=None):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = (
            session.query(Item.item_id, Item.title, Movie.medium, Movie.runtime, Branch.branch_name, Item.status)
            .join(Movie, Movie.isan == Item.isan) # joining movie table for medium and runtime
            .join(Branch, Branch.branch_id == Item.branch_id)
            .filter(Item.title.ilike(f'%{title}%') if title else True) # Case insensitive search, only active if value not None
            .filter(Item.genre == genre if genre else True) # looks for exact genre, only active if value not None
            .filter(Item.isan == isan if isan else True) # looks for exact isan, only active if value not None
            .filter(Movie.runtime <= runtime if runtime else True) # looks for runtime <= specified runtime, only active if value not None
            .filter(Branch.branch_id == branch if branch else True) # looks for exact branch 
            .all()  # Call the method to execute the query
        )
    print(query)
    return query


# all customer information by id, including all items chekced out by them, both id and title
def get_patron_by_id(patron_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # get patron info
        patron = session.query(Patron).filter(Patron.patron_id == patron_id).first()
        patron_name = patron.patron_name
        phone = patron.phone
        account_type = patron.account_type
        limit_reached = patron.limit_reached
        
        # get branch info
        branch_id = patron.branch_id
        branch = session.query(Branch).filter(Branch.branch_id == branch_id).first()
        branch_name = branch.branch_name
        
        # get items
        items = session.query(Item.item_id, Item.title).filter(Item.patron_id == patron_id).all()

    result_dict = {
        'name': patron_name,
        'phone': phone,
        'account_type': account_type,
        'branch_name': branch_name,
        'limit_reached': limit_reached,
        'checked_out_items': items
        }
    return result_dict # returns a dict, checked out items is a list of tuples

# Add patron
def add_patron(branch_id, patron_name, phone_value, account_type):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_patron = Patron(patron_name=patron_name, branch_id=branch_id, phone=phone_value, account_type=account_type) # create patron object
        session.add(new_patron) # write it to the database
        session.commit() # commit changes
        session.refresh(new_patron) # refresh to get the id


# Add book
def add_book(branch_id, isbn, title, genre, medium, pages, author_name):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # check for author in db (case insensitive)
        existing_author = session.query(Author).filter(func.lower(Author.author_name) == func.lower(author_name)).first() # first becasue there should only be one, mispelled authors will be entered as a new one
        
        if existing_author:
            # retrieve id if author exists
            author_id = existing_author.author_id
        else:
            # add author
            new_author = Author(author_name=author_name)
            session.add(new_author)
            session.commit()
            session.refresh(new_author)
            author_id = new_author.author_id
            
        # create the item
        new_item=Item(branch_id=branch_id, isbn=isbn, item_type='book', status='available', title=title, genre=genre)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        
        # check if book already exists
        existing_book = session.query(Book).filter(Book.isbn == isbn).first()
        if existing_book:
            return
        else:
            # add book specific details
            new_book = Book(isbn=isbn, author_id=author_id, medium=medium, pages=pages)
            session.add(new_book)
            session.commit()


# Add movie
def add_movie(branch_id, isan, title, genre, runtime, medium):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # add base item
        new_item = Item(branch_id=branch_id, isan=isan, item_type='movie', status='available', title=title, genre=genre)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        
        # check for existing movie
        existing_movie = session.query(Movie).filter(Movie.isan == isan).first()
        if existing_movie:
            return
        else:
            # add movie details
            new_movie = Movie(isan=isan, runtime=runtime, medium=medium)
            session.add(new_movie)
            session.commit()


# Remove Item
def remove_item(item_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # get item
        item = session.query(Item).filter(Item.item_id == item_id).first()
        if not item:
            return False
        isbn = item.isbn
        isan = item.isan
        
        # remove item
        session.query(Item).filter(Item.item_id == item_id).delete()
        
        # remove book details if book
        if isbn:
            session.query(Book).filter(Book.isbn == isbn).delete()
        
        # remove movie details if movie
        if isan:
            session.query(Movie).filter(Movie.isan == isan).delete()
            
        session.commit()

 
# Check out
def check_out(item_id, patron_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # retrieve the patron
        patron = session.query(Patron).filter(Patron.patron_id == patron_id).first()
        if not patron or patron.limit_reached:
            return False
        
        # retrieve the item
        item = session.query(Item).filter(Item.item_id == item_id).first()
        if not item or item.status == 'checked out':
            return False
        
        # check limit
        account_type = patron.account_type
        amount_checked_out = session.query(func.count(Item.item_id)).filter(Item.patron_id == patron_id).scalar()
        
        if account_type == "Adult" and amount_checked_out >= 5:
            return False
        elif account_type == "Child" and amount_checked_out >= 3:
            return False
        
        # change status
        item.status = 'checked out'
        
        # add patron
        item.patron_id = patron_id
        
        # recount and lock account on limits
        amount_checked_out += 1
        if account_type == "Adult" and amount_checked_out >= 5:
            patron.limit_reached = True
        elif account_type == "Child" and amount_checked_out >= 3:
            patron.limit_reached = True
        
        session.commit()
        
        
# Return
def return_item(item_id, patron_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # retrieve the item
        item = session.query(Item).filter(Item.item_id == item_id).first()
        if not item or item.status == 'available':
            return False
        
        # retrieve the patron
        patron = session.query(Patron).filter(Patron.patron_id == patron_id).first()
        if not patron:
            return False
        
        
        # change status
        item.status = 'available'
        
        # remove patron
        item.patron_id = None
        
        # check if below limit
        account_type = patron.account_type
        amount_checked_out = session.query(func.count(Item)).filter(Item.patron_id == patron_id).scalar()
        if account_type == "Adult" and amount_checked_out < 5:
            patron.limit_reached = False
        elif account_type == "Child" and amount_checked_out < 3:
            patron.limit_reached = False
        
        session.commit()


# add late fee
def add_fee(patron_id, fees):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # retrieve the patron
        patron = session.query(Patron).filter(Patron.patron_id == patron_id).first()
        if not patron:
            return False
        
        # lock account
        patron.limit_reached = True
        
        # add fees
        fees = Decimal(str(fees))
        patron.fees += fees
        
        session.commit()


# pay late fee
def pay_fee(patron_id, payment):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        patron = session.query(Patron).filter(Patron.patron_id == patron_id).first()
        if not patron:
            return False
        
        payment = Decimal(str(payment))
        patron.fees -= payment
        
        # check for balance and unlock account if 0
        if patron.fees == 0:
            patron.limit_reached = False
        
        session.commit()
        
        
# remove account
def remove_patron(patron_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # remove patron
        session.query(Patron).filter(Patron.patron_id == patron_id).delete()
        session.commit()


# get branch names
def get_branch_names():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        branch_names = session.query(Branch.branch_name).all()
        branch_names = [branch_name[0] for branch_name in branch_names]
        return branch_names # returns list of branch names

    
# get genres
def get_genres():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        genres = session.query(Item.genre).distinct().all()
        genres = [genre[0] for genre in genres]
        return genres # returns a list of genres
