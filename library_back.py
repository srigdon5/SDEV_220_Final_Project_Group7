from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

# create app
app = Flask(__name__)


# create db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# main item class
class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # main item id, will autoincrement when an item is added
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.branch_id'), nullable=False) # id of the branch the item is located
    patron_id = db.Column(db.Integer, db.ForeignKey('patron.patron_id'), nullable=True) # id of patron who currently has itemchecked out, null when not checked out
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn'), nullable=True) # isbn of book, null for movies
    isan = db.Column(db.String(12), db.ForeignKey('movie.isan'), nullable=True) # isan of movie, null for books
    item_type = db.Column(db.String(5), nullable=False) # the type of item, either book or movie
    status = db.Column(db.String(11), nullable=False) # if the item is checked out, either available or checked out
    title = db.Column(db.String(50), nullable=False) # title of the item
    
    # constraints on data
    __table_args__ = (
        db.CheckConstraint("item_type IN ('book','movie')"),
        db.CheckConstraint("status IN ('available','checked out')")
        )
    
    def __repr__(self):
        return f"{self.item_id}, {self.title}"
    

# book item class
class Book(db.Model):
    isbn = db.Column(db.String(13), primary_key=True) # isbn of book, acts as primary key since it is unique
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), nullable=False) # id of author who wrote the book
    medium = db.Column(db.String(11), nullable=False) # The format the itemis in, must be ebook, paperback, hard cover, or large print
    pages = db.Column(db.Integer) # the number of pages in the book
    ar = db.Column(db.Boolean, nullable=False) # if the book is part of the Accelerated Reading (AR) program for students
    
    __table_args__ = (
        db.CheckConstraint("medium IN ('ebook','paperback','hard cover','large print','audiobook')")
    )
    
    def __repr__(self):
        return f"{self.isbn}"
   

# author class
class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # pk of author class, will autoincrement
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn'), nullable=False) # isbn of books written by this author
    author_name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"{self.author_id}, {self.author_name}"
    

# movie item class
class Movie(db.Model):
    isan = db.Column(db.String(12), primary_key=True) # ISAN of movie, acts as primary key since it is unique
    runtime = db.Column(db.Integer, nullable=False) # runtime of movie in minutes
    medium = db.Column(db.String(7), nullable=False) # format of the item, must be vhs, dvd, or blu-ray 
    
    __table_args__ = (
        db.CheckConstraint("medium IN ('vhs','dvd','blu-ray')")
    )
    
    def __repr__(self):
        return f"{self.isan}"
    

# patron class
class Patron(db.Model):
    patron_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # pk of patron class, will autoincrement
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'), nullable=True) # item_id of checked out item, if any
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.branch_id'), nullable=False) # branch _id of their home branch
    name = db.Column(db.String(30), nullable=False) # name of the patron
    phone = db.Column(db.String(14), nullable=False) # contact phone of patron
    account_type = db.Column(db.String(5), nullable=False) # The account type for determing check out limits, must be child or adult
    time = db.Column(db.Integer, nullable=True) # how long, in days, the item has been checked out for
    date = db.Column(db.DateTime, nullable=True) # the date the item was checked out, used to calculate time
    limit_reached = db.Column(db.Boolean, nullable=False, default=False) # Boolean indicating if the patron is at their check out limit
    fees = db.Column(db.Numeric(precision=5, scale=2), nullable=False, default=0.00) # the amount the patron owes in fees
    
    def __repr__(self):
        return f"{self.patron_id}, {self.name}"

# branch class
class Branch(db.Model):
    branch_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # pk of branch table, will auto increment
    address = db.Column(db.String(100), nullable=False) # address of branch location
    phone = db.Column(db.String(14), nullable=False) # phone number of branch