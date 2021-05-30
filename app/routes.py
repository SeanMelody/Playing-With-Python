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

    lengthSel = request.form["lengthSel"]

    lenghtInt = int(lengthSel)

    # capSel = request.form["capSel"]
    # charSel = request.form["charSel"]
    # numSel = request.form["numSel"]

    #     lengthSel = request.form["lengthSel"]

    custom_password = "Your custom password is: "

    charactersCust = string.ascii_letters + string.punctuation + string.digits

    passwordCust = "".join(random.sample(charactersCust, lenghtInt))

    return render_template("custom-password.html", password2=passwordCust, password=custom_password, length=lengthSel)

    #  length=lengthSel, capitals=capSel, characters=charSel, numbers=numSel
