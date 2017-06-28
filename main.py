from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

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
        self.email = email

@app.route('/', methods=['POST', 'GET'])
def index():



@app.route('/register')
def confirmation():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('welcome.html', title=title, username=username)

if __name__ == '__main__':
    app.run()
