from flask import Flask, request, jsonify
from utils.db import db, Blog, AllBlogs
import time

def create_post():
    data = request.get_json()
    userName = data['userName']
    title=data['title']
    body=data['body']
    imageURI=data['imageURI']
    if imageURI == 'INVALID':
        imageURI= None
    blogId=time.time()
    blogId=str(blogId)
    newBlog= Blog(blogId=blogId, title=title, body=body, imageURI=imageURI)
    newPost=AllBlogs(userName=userName,blogId=blogId)
    db.session.add(newBlog)
    db.session.add(newPost)
    try:
        db.session.commit()
        result ='Success'
    except:
        result= 'Database Commit Error'
    
    return result