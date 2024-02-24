from flask import Flask, request, jsonify, session
from utils.db import db, User

def log_in(userName, password):
    userExists = User.query.get(userName)
    if userExists == None:
        return "ERROR"
    if userExists.password != password :
        return "ERROR"

    session["userName"]=userName
    return "SUCCESS"