from flask import Flask, render_template, request, session

from common.database import Database
from models.user import User


app = Flask(__name__)  # '__main__'
app.secret_key = "jose"

@app.route('/')
def hello_method():
    return "Hello, world!"

@app.route('/login')
def login_template():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])

if __name__ == '__main__':
    app.run(port=4995, debug=True)
