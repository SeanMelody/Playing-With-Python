from flask import render_template
from app import app
import random
import string

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

