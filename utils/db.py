from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User table
class User(db.Model):
    userName = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(15), nullable=False)

    blogsCreated = db.relationship('AllBlogs', backref='user', cascade='all, delete-orphan')

# Blog table
class Blog(db.Model):
    blogId = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    body = db.Column(db.String(10000), nullable=False)
    imageURI = db.Column(db.String(500), nullable=True)

    blogsCreated = db.relationship('AllBlogs', backref='blog', cascade='all, delete-orphan')

# User vs Blog table
class AllBlogs(db.Model):
    userName = db.Column(db.String(50), db.ForeignKey('user.userName', ondelete='CASCADE'), primary_key=True)
    blogId = db.Column(db.String(50), db.ForeignKey('blog.blogId', ondelete='CASCADE'), primary_key=True)
    
