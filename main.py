from flask import Flask, jsonify, render_template, session
from datetime import timedelta
from functionalities.displayAll import *
from functionalities.createPost import *
from functionalities.signUp import *
from functionalities.login import *

from utils.db import db
from utils.seed import *

SESSION_WILL_BE_VALID = 1  # day

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_management.db'
app.secret_key = 'DebmalyaArshia'
app.permanent_session_lifetime = timedelta(days=SESSION_WILL_BE_VALID)
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
    data = display_all()
    print(data)
    try:
        flag = session['userName']
        flag = 1
    except:
        flag = 0
    return render_template('home.html', data=data, length = len(data), flag=flag)
    # return jsonify(display_all())

@app.route('/login', methods = ['POST'])
def login():
    #return render_template('login.html')
    return jsonify(log_in())

@app.route('/signup', methods=['POST'])
def signup():
    return jsonify(sign_up())
    #return render_template('signup.html')


"""
this function is for creating a new post for a logged in user
"""
@app.route('/createPost', methods=['POST'])
def create():
    return jsonify(create_post())

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/logout')
def logout():
    if "userName" in session:
        session.pop('userName', None)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
    with app.app_context():
        #db.drop_all()
        db.create_all()
    app.run(debug=True)