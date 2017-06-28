from flask import Flask, request, redirect, render_template
import cgi

# Initialize the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True

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
        #Validation
        ans = "good"
        ans = validateUserName(username)
        ans = validatePassword(password)
        ans = validateVerify(verify)

        if ans == "good":
            return render_template('welcome.html', user_name=username,
 user_name_error=username_error, password_error=password_error,
 verify_error=verify_error)
        else:
            return redirect('/error?username=' + username + ' ' + ans)
    else:
        return render_template('register.html')

@app.route('/register')
def confirmation():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('welcome.html', title=title, username=username)

def validateUserName(userName):
    if userName and not userName.isspace():
        if " " in username:
            return "Username cannot contain any spaces."
    else:
        return "Username cannot be blank."

def validatePassword(passWord):
    if userName and not userName.isspace():
        if not (3 <= number <= 20):
            return "Password must be between 3 and 20 characters."
        if " " in password:
            return "Password cannot contain any spaces."
    else:
        return "Password cannot be blank."

def validateVerify(verify):
    if verify and not verify.isspace():
        if " " in verify:
            return "Verify password cannot contain any spaces."
    else:
        return "Verify password cannot be blank."


app.run()
