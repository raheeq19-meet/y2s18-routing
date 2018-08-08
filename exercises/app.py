from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<int:id>')
def display_student(id):
    return render_template('student.html' ,student_id=id)

@app.route('/')
def home_route(name):
    return render_template('')
app.run(debug=True)
