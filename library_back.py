from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

# create app
app = Flask(_name_)


# create db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# main item class
class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # main item id, will autoincrement when an item is added
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.branch_id')) # id of the branch the item is located
    patron_id = db.Column(db.Integer, db.ForeignKey('patron.patron_id'), nullable=True) # id of patron who currently has itemchecked out, null when not checked out
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn'), nullable=True) # isbn of book, null for movies
    isan = db.Column(db.String(13), db.ForeignKey('movie.isan'), nullable=True) # isan of movie, null for books
    item_type = db.Column(db.String(5)) # the type of item, either book or movie
    status = db.Column(db.String(11)) # if the item is checked out, either available or checked out
    title = db.Column(db.String(50)) # title of the item
    
    # constraints on data
    __table_args__ = (
        db.CheckConstraint("item_type IN ('book','movie')")
        db.CheckConstraint("status IN ('available','checked out')")
        )
    
    def __repr__:
        return f"item {self.item_id}, {self.title}"
    

# book item class
class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True) # isbn of book, acts as primary key since it is unique
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id')) # id of item as found in the 