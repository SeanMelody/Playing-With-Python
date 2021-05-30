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

    lengthSel = "10"

    lengthSel = request.form["lengthSel"]

    lenghtInt = int(lengthSel)

    custom_password = "Your custom password is: "

    charactersCust = string.ascii_letters + string.punctuation + string.digits

    passwordCust = "".join(random.sample(charactersCust, lenghtInt))

    return render_template("custom-password.html", password2=passwordCust, password=custom_password)

    #  length=lengthSel, capitals=capSel, characters=charSel, numbers=numSel, test=test


@app.route("/custom-test/", methods=["POST"])
def custom_test():

    lengthSel = "10"
    capSel = "A"
    charSel = "B"
    numSel = "C"

    lengthSel = request.form["lengthSel"]
    # capSel = request.form["capSel"]

    lenghtInt = int(lengthSel)

    capSel = request.form["capSel"]
    charSel = request.form["charSel"]
    numSel = request.form["numSel"]

    # testSel = request.form["testSel"]

    # test = "unchecked"

    # if testSel:
    #     test = "checked"
    #     lengthSel = request.form["lengthSel"]

    custom_password = "Your custom password is: "

    charactersCust = string.ascii_letters + string.punctuation + string.digits

    passwordCust = "".join(random.sample(charactersCust, lenghtInt))

    return render_template("custom-test.html", password2=passwordCust, password=custom_password, capitals=capSel, characters=charSel, numbers=numSel, length=lengthSel)

    #  length=lengthSel, capitals=capSel, characters=charSel, numbers=numSel, test=test
