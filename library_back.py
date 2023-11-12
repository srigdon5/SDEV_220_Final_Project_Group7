from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

# create app
app = Flask(_name_)


# create db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# main item class
class Item(db.Model):
    item_id=db.Column(db.Integer, primary_key=True, autoincrement=True) # main item id, will autoincrement when an item is added
    branch_id=db.Column(db.Integer, db.ForeginKey('branch.branch_id')) # id of the branch the item is located
    patron_id=db.Column(db.Integer, db.ForeginKey('patron.patron_id'), nullable=True) # 
    