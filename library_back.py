from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

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


###### SEARCH FUNCTIONS
def search_items_by_title(search):
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        query = (
            session.query(Item.title, Item.item_type, Item.branch_id, Item.status) # retrieve title, type, branch_id and status
            .filter(Item.title.ilike(f'%{search}%')) # Case insensitive search
            .all # retrieves all items
        )
        
        result = [(title, item_type, branch_id, status) for title, item_type, branch_id, status in query]
    
    return result


def search_items_by_title_branch(search, branch_id):
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        query = (
            session.query(Item.title, Item.item_type, Item.status) # retrieve title, type, and status
            .filter(Item.title.ilike(f'%{search}%')) # Case insensitive search
            .filter(Item.branch_id == branch_id) # limits it to a specific branch
            .all # retrieves all items
        )
        
        result = [(title, item_type, status) for title, item_type, status in query]
    
    return result


# retrieve all item information based on id
def get_item_by_id(item_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        item = session.query(Item).filter(Item.item_id == item_id).first()
        
    return item


# search all books based on a search term where the term is the title
def search_books(search):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = (
            session.query(Item.title, Author.author_name, Book.medium, Book.pages)
            .join(Author, Author.isbn == Book.isbn) # joining the author table for author info
            .join(Book, Book.isbn == Item.isbn) # joining the book table for medium and pages
            .filter(Book.title.ilike(f'%{search}%'))  # Case insensitive search
            .all()  # Call the method to execute the query
        )
        result = [(title, author_name, medium) for title, author_name, medium in query]
    return result


# same as book search but movies
def search_movies(search):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = (
            session.query(Item.title, Movie.medium, Movie.runtime)
            .join(Movie, Movie.isan == Item.isan) # joining movie table for medium and runtime
            .filter(Item.title.ilike(f'%{search}%'))  # Case insensitive search
            .all()  # Call the method to execute the query
        )
        result = [(title, author_name, medium) for title, author_name, medium in query]
    return result


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
        items = session.query(Item.title).filter(Item.patron_id == patron_id).all()

    result_dict = {
        'name': patron_name,
        'phone': phone,
        'account_type': account_type,
        'branch_name': branch_name,
        'limit_reached': limit_reached,
        'checked_out_items': items
        }
    print(result_dict)
    return result_dict

# Add patron
def add_patron(branch_id, name, phone, account_type):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_patron = Patron(name=name, branch_id=branch_id, phone=phone, account_type=account_type) # create patron object
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
        
        # add book specific details
        new_book = Book(isbn=isbn, author_id=author_id, medium=medium, pages=pages)
        session.add(new_book)
        session.commit()


# Remove Book
def remove_book(item_id, isbn):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # remove item
        session.query(Item).filter(Item.item_id == item_id).delete()
        
        # remove book details
        session.query(Book).filter(Book.isbn == isbn).delete()
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
        
        # add movie details
        new_movie = Movie(isan=isan, runtime=runtime, medium=medium)
        session.add(new_movie)
        session.commit()


# Remove Movie
def remove_movie(item_id, isan):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # remove item
        session.query(Item).filter(Item.item_id == item_id).delete()
        
        # remove book details
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
        
        # change status
        item.status = 'checked out'
        
        # add patron
        item.patron_id = patron_id
        
        session.commit()
        
        
# Return
def return_item(item_id, patron_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # retrieve the item
        item = session.query(Item).filter(Item.item_id == item_id).first()
        if not item or item.status == 'available':
            return False
        
        # change status
        item.status = 'available'
        
        # remove patron
        item.patron_id = None
        
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
        patron.fees += fees
        
        session.commit()


# pay late fee
def pay_fee(patron_id, payment):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        patron = session.query(Patron).filter(Patron.patron_id == patron_id).first()
        if not patron:
            return False
        
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
