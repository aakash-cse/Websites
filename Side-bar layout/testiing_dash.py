from flask import Flask
from flask import render_template
from flask import request
from flask import request, redirect, render_template, url_for
import json
from dashboard import *
from mail import email_content
from log_load import verify
from extra import write_log
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def dash():
    data = 'Main_content is displayed here'
    user = "Dummy check"
    return render_template("dash_board.html",data=data,user=user)
@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    data = 'statistics Content is displayed'
    user = "Dummy check"
    return render_template("dash_board.html",data=data,user=user)
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    data = 'profile Content is displayed'
    user = "Dummy check"
    return render_template("dash_board.html",data=data,user=user)
@app.route('/sent', methods=['GET', 'POST'])
def sent():
    data = 'sent page'
    user = "Dummy check"
    return render_template("dash_board.html",data=data,user=user)
@app.route('/today_schedule', methods=['GET', 'POST'])
def today_schedule():
    data = 'today_schedule page'
    user = "Dummy check"
    return render_template("dash_board.html",data=data,user=user)
@app.route('/about', methods=['GET', 'POST'])
def about():
    data = 'about the authors of the website'
    user = "Dummy check"
    return render_template("dash_board.html",data=data,user=user)


if __name__ == '__main__':
    global candidate_id
    app.run(host='127.0.0.1', port=8080, debug=True)
