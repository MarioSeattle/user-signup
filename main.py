from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://signup:sounders@localhost:8889/signup'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)


    def __init__(self, username, password, email):
        self.username = username
        self.password = password

@app.route("/", methods=['POST','GET'])
def index():
    if request.method=="POST":
        #initialize error vairables as empty strings 
        username_error = ""
        password_error = ""
        verify_error = ""
        #Input from the form (POST)
        username = cgi.escape(request.form['username'], quote=True)
        password = cgi.escape(request.form['password'], quote=True)
        verify = cgi.escape(request.form['verify'], quote=True)
        #UserName Validation
        if username == "":
            username_error = "Please enter a valid username."
        if len(username) > 20:
            username_error = "Username must be less than 20 characters."
        if len(username) < 3:
            username_error = "Username must be more than 3 characters."
        if " " in username:
            username_error = "Username cannot contain any spaces."
        #Password validate
        if password == "":
            password_error = "Please enter a valid password."
        if len(password) > 20:
            password_error = "Password must be less than 20 characters."
        if len(password) < 3:
            password_error = "Password must be more than 3 characters."
        if " " in username:
            password_error = "Password cannot contain any spaces."
        #Password verify
        if verify != password:
            verify_error = "Passwords must match."
        if username_error == "" and password_error == "" and verify_error == "":
            return redirect('/welcome?username=' + username)

        return render_template('welcome.html', user_name=username, user_name_error=username_error, password_error=password_error, verify_error=verify_error)
    else:
        return render_template('register.html')

@app.route('/register')
def confirmation():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('welcome.html', title=title, username=username)

app.run()
