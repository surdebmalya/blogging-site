from flask import jsonify
from utils.db import db, User, Blog, AllBlogs 

def seeding_database():
    user_details = [
        {
            'userName': 'Arshia',  
            'email': 'chaudhuri.arshia@gmail.com',
            'password':'Abc123!'
        },
        {
            'userName': 'Debmalya', 
            'email': 'sur.debmalya@gmail.com',
            'password': '453@gjD'

        },
        {
            'userName': 'Shikha', 
            'email': 'roy.sikha123@gmail.com',
            'password': 'fhD%48'

        }
        
    ]
    
    for user_data in user_details:
        new_User = User(
            userName = user_data['userName'],
            email = user_data['email'],
            password=user_data['password']
            )
        db.session.add(new_User)

    db.session.commit()
    

    blog_details = [
        {
            'blogId': '1708776842.172973',
            'title': 'Filmfare Award 2024',
            'body': 'Vikrant Massey truly deserved the award for his acting in 12th Fail.',
            'imageURI': None
        },
        {
            'blogId': '1708776865.609455',
            'title': '2024 Election',
            'body': 'I am waiting for the results of the election.',
            'imageURI': None
        },
        
    ]

    for blog_data in blog_details:
        new_blog = Blog(
            blogId = blog_data['blogId'],
            title = blog_data['title'],
            body=blog_data['body'],
            imageURI=blog_data['imageURI']
            )
        db.session.add(new_blog)

    db.session.commit()

    post_details = [
        {
            "userName": 'Arshia',
            "blogId": '1708776842.172973'
        },
        {
            "userName": 'Debmalya',
            "blogId": '1708776865.609455'
        }        
    ]
    for post_data in post_details:
        new_post = AllBlogs(
            userName = post_data['userName'],
            blogId = post_data['blogId']
            )
        db.session.add(new_post)

    db.session.commit()
    return {'message': 'Success'}