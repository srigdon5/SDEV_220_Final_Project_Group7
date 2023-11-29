from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# create engine and base
engine = create_engine('sqlite:///data.db')
Base = declarative_base(bind=engine)

# main item class
class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True, autoincrement=True)  # main item id, will autoincrement when an item is added
    branch_id = Column(Integer, ForeignKey('branch.branch_id'), nullable=False)  # id of the branch the item is located
    patron_id = Column(Integer, ForeignKey('patron.patron_id'), nullable=True)  # id of patron who currently has item checked out, null when not checked out
    isbn = Column(String(13), ForeignKey('book.isbn'), nullable=True)  # isbn of book, null for movies
    isan = Column(String(12), ForeignKey('movie.isan'), nullable=True)  # isan of movie, null for books
    item_type = Column(String(5), nullable=False)  # the type of item, either book or movie
    status = Column(String(11), nullable=False)  # if the item is checked out, either available or checked out
    title = Column(String(50), nullable=False)  # title of the item
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
    ar = Column(Boolean, nullable=False)  # if the book is part of the Accelerated Reading (AR) program for students
    
    __table_args__ = (
        CheckConstraint("medium IN ('ebook','paperback','hard cover','large print','audiobook')")
    )
    
    def __repr__(self):
        return f"{self.isbn}"


# author class
class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True, autoincrement=True)  # pk of author class, will autoincrement
    isbn = Column(String(13), ForeignKey('book.isbn'), nullable=False)  # isbn of books written by this author
    author_name = Column(String(50), nullable=False)
    
    def __repr__(self):
        return f"{self.author_id}, {self.author_name}"


# movie item class
class Movie(Base):
    __tablename__ = 'movie'
    isan = Column(String(12), primary_key=True)  # ISAN of movie, acts as primary key since it is unique
    runtime = Column(Integer, nullable=False)  # runtime of movie in minutes
    medium = Column(String(7), nullable=False)  # format of the item, must be vhs, dvd, or blu-ray 
    
    __table_args__ = (
        CheckConstraint("medium IN ('vhs','dvd','blu-ray')")
    )
    
    def __repr__(self):
        return f"{self.isan}"


# patron class
class Patron(Base):
    __tablename__ = 'patron'
    patron_id = Column(Integer, primary_key=True, autoincrement=True)  # pk of patron class, will autoincrement
    item_id = Column(Integer, ForeignKey('item.item_id'), nullable=True)  # item_id of checked out item, if any
    branch_id = Column(Integer, ForeignKey('branch.branch_id'), nullable=False)  # branch _id of their home branch
    name = Column(String(30), nullable=False)  # name of the patron
    phone = Column(String(14), nullable=False)  # contact phone of patron
    account_type = Column(String(5), nullable=False)  # The account type for determining check out limits, must be child or adult
    time = Column(Integer, nullable=True)  # how long, in days, the item has been checked out for
    date = Column(DateTime, nullable=True)  # the date the item was checked out, used to calculate time
    limit_reached = Column(Boolean, nullable=False, default=False)  # Boolean indicating if the patron is at their check out limit
    fees = Column(Numeric(precision=5, scale=2), nullable=False, default=0.00)  # the amount the patron owes in fees
    
    def __repr__(self):
        return f"{self.patron_id}, {self.name}"


# branch class
class Branch(Base):
    __tablename__ = 'branch'
    branch_id = Column(Integer, primary_key=True, autoincrement=True)  # pk of branch table, will auto increment
    address = Column(String(100), nullable=False)  # address of branch location
    phone = Column(String(14), nullable=False)  # phone number of branch
    
    def __repr__(self):
        return f"{self.branch_id} {self.address} {self.phone}"



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