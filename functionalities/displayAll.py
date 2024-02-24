from flask import Flask, request, jsonify
import json
from utils.db import db, Blog, AllBlogs

def display():
    blogs = AllBlogs.query.all()

    result=[]
    for blog in in blogs:
        uname=blog.userName
        bid=blog.blogId
        blogData=Blog.query.get(bid)
        blogTitle=blogData.title
        blogBody=blogData.body
        result.append(
            "userName":uname,
            "title": blogTitle,
            "body":blogBody
        )
    
    reverse(result)
    return result