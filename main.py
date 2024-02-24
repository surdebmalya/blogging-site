from flask import Flask, jsonify, render_template
from functionalities.displayAll import *
from functionalities.createPost import *
from utils.db import db
from utils.seed import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_management.db'
db.init_app(app)

@app.route('/seed')
def seeding():
    return jsonify(seeding_database())

"""
this function is for displaying all the blog posts on opening the app
"""
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    # return jsonify(display_all())

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


"""
this function is for creating a new post for a logged in user
"""
@app.route('/createPost', methods=['POST'])
def create():
    return jsonify(create_post())


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)