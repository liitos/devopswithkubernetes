from app import db

class Pings(db.Model):
    __tablename__ = 'pings'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))

