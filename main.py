from flask import Flask, jsonify, render_template, session, redirect, url_for, request
from datetime import timedelta
from functionalities.displayAll import *
from functionalities.createPost import *
from functionalities.signUp import *
from functionalities.login import *
from functionalities.fetch import *
from utils.db import db
from utils.seed import *
from utils.extra import *

SESSION_WILL_BE_VALID = 1 # day

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_management.db'
app.secret_key = 'DebmalyaArshia'
app.permanent_session_lifetime = timedelta(days=SESSION_WILL_BE_VALID)
db.init_app(app)

@app.route('/seed')
def seeding():
    try:
        return jsonify(seeding_database())
    except:
        return jsonify({'message': 'Already seeded'})

"""
this function is for displaying all the blog posts on opening the app
"""
@app.route('/')
@app.route('/home')
def home():
    data = display_all()
    data = shorten_text(data)
    print(data)
    return render_template('home.html', data=data, length = len(data), called_function="home")

"""
this function will help to show the error message to the users
"""
@app.route('/error')
def error():
    return render_template('error.html')

"""
here all login functionalities will be added
"""
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if "userName" in session:
            return redirect(url_for("home"))
        else:
            return render_template('login.html')
    elif request.method == 'POST':
        userName = request.form["username"]
        password = request.form["password"]
        res = log_in(userName, password)
        if res=="SUCCESS":
            return redirect(url_for("home"))
        else:
            return redirect(url_for("error"))

"""
here all signup functionalities will be added
"""
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method== 'GET':
        if "userName" in session:
            return redirect(url_for("home"))
        else:
            return render_template('signup.html')
    elif request.method == 'POST':
        userName = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        res = sign_up(userName, email, password)
        if res=="SUCCESS":
            return redirect(url_for("home"))
        else:
            return redirect(url_for("error"))

"""
jot down all the writing activities
"""
@app.route('/write')
def write():
    if "userName" in session:
        return render_template('blog_create.html')
    else:
        return redirect(url_for("home"))

@app.route('/write', methods=['POST'])
def posting():
    userName = session['userName']
    title = request.form["blogTitle"]
    content = request.form["blogContent"]
    imageURI = 'INVALID'
    res = create_post(userName, title, content, imageURI)
    if res=="SUCCESS":
        return redirect(url_for("home"))
    else:
        return redirect(url_for("error"))

"""
blog rendering
"""
@app.route('/blog/<string:blogId>')
def blog(blogId):
    # author, title, body 
    blogs = AllBlogs.query.all()
    for blog in blogs:
        if blog.blogId== blogId:
            userName= blog.userName
            break
    blogDetail= Blog.query.get(blogId)
    title = blogDetail.title
    body = blogDetail.body
    return render_template('blog.html', title=title, author=userName, content=body)

@app.route('/my-blog')
def myblog():
    if "userName" in session:
        userName= session["userName"]
        res = fetch_for_single_user(userName)
        res = shorten_text(res)
        return render_template('home.html', data=res, length = len(res), called_function="myblog")
    else:
        return render_template('login.html')

@app.route('/user/<string:userName>')
def userblog(userName):
    try:
        res = fetch_for_single_user(userName)
        res = shorten_text(res)
        return render_template('home.html', data=res, length = len(res), called_function="userblog")
    except:
        return redirect(url_for("error"))

"""
logout
"""
@app.route('/logout')
def logout():
    if "userName" in session:
        session.pop('userName', None)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True)