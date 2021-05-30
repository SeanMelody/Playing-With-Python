from flask import render_template, request
from app import app
import random
import string
enctype = "multipart/form-data"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/new-password/')
def new_password():

    characters = string.ascii_letters + string.punctuation + string.digits

    password = "".join(random.sample(characters, 15))

    print("hello world")

    return render_template("new-password.html", password=password)
    # return password

# @app.route("/custom-password", methods=["POST"])


@app.route("/custom-password/", methods=["POST"])
def custom_password():

    lengthSel = "0"

    lengthSel = request.form["lengthSel"]

    lenghtInt = int(lengthSel)

    password_desc = "Your custom password is: "

    charactersCust = string.ascii_letters + string.punctuation + string.digits

    passwordCust = "".join(random.sample(charactersCust, lenghtInt))

    return render_template("custom-password.html", password=passwordCust, password_desc=password_desc)


@app.route("/custom-test/")
def custom_test():

    return render_template("custom-test.html")
