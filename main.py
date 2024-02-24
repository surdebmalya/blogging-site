from flask import Flask, jsonify
from functionalities import *

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_management.db'
# db.init_app(app)

"""
this function is for displaying all the blog posts on opening the app
"""
@app.route('/')
@app.route('/home')
def index0():
    return jsonify(displayAll())

@app.route('/createPost', methods=['POST'])
def create():
    return jsonify(createPost())

if __name__ == '__main__':
    app.run(debug=True)