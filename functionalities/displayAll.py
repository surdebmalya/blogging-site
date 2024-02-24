from flask import Flask, request, jsonify
import json
from utils.db import db, Blog, AllBlogs

def display_all():
    blogs = AllBlogs.query.all()

    result=[]
    for blog in blogs:
        userName=blog.userName
        blogId=blog.blogId
        blogData=Blog.query.get(blogId)
        blogTitle=blogData.title
        blogBody=blogData.body
        blogImageURI=blogData.imageURI
        post={}
        post["userName"] = userName
        post["blogId"] = blogId
        post["title"] = blogTitle
        post["body"] = blogBody
        post["imageURI"] = blogImageURI
        result.append(post)
    
    result = result[::-1]
    return result