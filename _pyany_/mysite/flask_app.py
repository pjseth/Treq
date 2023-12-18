from flask import Flask, render_template, request, jsonify
import json
import os
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()
template_dir = os.path.join(THIS_FOLDER, "templates")
static_dir = os.path.join(THIS_FOLDER, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def hello_world():
   return 'Hello, World!'

@app.route('/create.html')
def create():
   return render_template('create.html')

@app.route('/home.html')
def home():
   return render_template('home.html')

@app.route('/inprogress.html')
def inprogress():
   return render_template('inprogress.html')

@app.route('/invite-friends.html')
def inviteFriends():
   return render_template('invite-friends.html')

@app.route('/login.html')
def login():
   return render_template('login.html')

@app.route('/onboarding.html')
def onboarding():
   return render_template('onboarding.html')

@app.route('/signup.html')
def signup():
   return render_template('signup.html')

@app.route('/user.html')
def user():
   return render_template('user.html')

@app.route('/rank.html')
def rank():
   return render_template('rank.html')

@app.route('/newplace.html')
def newPlace():
   return render_template('newplace.html')

@app.route('/japan.html')
def japan():
   return render_template('japan.html')


if __name__ == '__main__':
   app.run(debug=True)