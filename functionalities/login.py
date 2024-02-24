from flask import Flask, request, jsonify, session
from utils.db import db, User

def log_in():
    data = request.get_json()
    userName=data['userName']
    password = data['password']
    userExists = User.query.get(userName)
    if userExists == None:
        return "ERROR"
    if userExists.password != password :
        return "Error"

    session["userName"]=userName
    return "Success!"