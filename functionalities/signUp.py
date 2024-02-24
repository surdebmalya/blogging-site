from flask import Flask, request, jsonify, session
from utils.db import db, User

def sign_up():
    data = request.get_json()
    userName= data['userName']
    email = data ['email']
    password = data ['password']
    userExists= User.query.get(userName)
    emailExists = User.query.get(email)
    if userExists == None and emailExists == None:
        newUser = User(
            userName= userName,
            email= email,
            password = password
        )
        db.session.add(newUser)
        db.session.commit()
    else:
        return "ERROR"
    
    session["userName"]=userName
    return "Success!"
    