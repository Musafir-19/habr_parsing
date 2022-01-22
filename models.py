from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'habr_posts'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    comments = db.Column(db.String, nullable=False)
