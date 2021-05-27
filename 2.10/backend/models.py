from app import db

class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))

