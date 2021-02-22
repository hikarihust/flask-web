from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("first_page.html")

@app.route("/second")
def hello_world_fancy():
    return render_template("second_page.html")

@app.route("/template")
def template():
    template=Template("Hello, {{name}}")
    return template.render(name="John")

@app.route("/jinja")
def jinja_intro():
    return render_template(
            "jinja_intro.html", name="John", template_name="Jinja2"
        )

@app.route("/expressions")
def expressions():
    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"
    
    # addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = "Caption"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }

    return render_template(
            "expressions.html", **kwargs
        )