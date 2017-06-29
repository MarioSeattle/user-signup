from flask import Flask, request, redirect, render_template
import cgi

# Initialize the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "GET":
        return render_template('register.html')
    #Input from the form (POST)
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    username_error = ""
    password_error = ""
    verify_error = ""
    #if username and not username.isspace():
    if " " in username:
        username_error = "Username cannot contain any spaces."
    #    username_error = "Username cannot be blank."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters."
    #if username and not username.isspace():
    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters."
    elif " " in password:
        password_error = "Password cannot contain any spaces."
    #if verify and not verify.isspace():
    if verify != password:
        verify_error= "Password does not match!"
    elif not username_error and not password_error and not verify_error: 
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('register.html', username=username, username_error=username_error, password_error=password_error, verify_error=verify_error)
#this handler will render the welcome user 
@app.route('/welcome')
def welcome():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('welcome.html', title=title, username=username)

app.run()
