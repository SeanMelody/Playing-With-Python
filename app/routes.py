from flask import render_template
from app import app
import random
import string

@app.route('/')

def index():
        return render_template("index.html")





@app.route('/new-password/')
def new_password():
# def index():
#     return "Hello, World!"
# def index():

        characters = string.ascii_letters + string.punctuation + string.digits


        password = "".join(random.sample(characters, 15))



        print("hello world")

        # user = {'username': 'Arya'}





        return password

        # return render_template('index.html', title='Home', user=user, password=password)