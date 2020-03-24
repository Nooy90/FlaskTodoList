from app import *

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)