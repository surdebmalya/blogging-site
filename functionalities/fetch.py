from flask import Flask, request, jsonify
import json
from utils.db import db, Blog, AllBlogs

def fetch_for_single_user(userName):
    blogs = AllBlogs.query.all()
    listOfId=[]
    for each in blogs:
        if userName == each.userName:
            listOfId.append(each.blogId)

    ## return list of all blogs
    res=[]
    for each in listOfId:
        post = Blog.query.get(each)
        res.append({
            "userName" : userName,
            "blogId": each,
            "title" : post.title,
            "body" : post.body}
        )
    res = res[::-1]
    return res
