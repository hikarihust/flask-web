from flask import Flask, render_template


app = Flask(__name__)  # '__main__'


@app.route('/')
def hello_method():
    return "Hello, world!"

@app.route('/login')
def login_template():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=4995, debug=True)
