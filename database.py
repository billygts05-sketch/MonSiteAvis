from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Kim(db.Model):
    __tablename__ = 'kim'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    text = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String)