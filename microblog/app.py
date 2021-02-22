import datetime
from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first=first
        self.second=second
        self.third=third
        self.fourth=fourth
    
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
    return render_template("home.html")

@app.route("/first")
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

@app.route("/data-structures")
def render_data_structures():
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A beautiful Mind"
    ]
    car = {
        "brand": "Tesla",
        "model": "Roadstar",
        "year": "2020"
    }
    moons=GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons
    }
    return render_template(
            "data_structures.html", **kwargs
        )

@app.route("/conditionals-basics")
def render_conditionals():
    company = True
    return render_template("conditionals_basics.html", company=company)

@app.route("/for-loop")
def render_for_loop():
    planets = [
        "Mercury",
        "Venus",
        "Earch",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop/conditionals")
def render_loops_and_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Sal": "Windows",
    }
    return render_template("loops_and_conditionals.html", user_os=user_os)
