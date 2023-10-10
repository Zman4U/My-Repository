# Import Flask modules
from flask import Flask, render_template 
# Create an object named app
app = Flask(__name__)

# Create welcome page with main.html file and assing it to the root path
@app.route("/")
def head():
    first = "This is my first conditions experioence"
    return render_template("index.html", message = first)

# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised


# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')


# Add a statement to run the Flask application which can be reached from any host.
