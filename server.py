# Connects to front end server
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/day')
def distilling_day():
     # Get information from database to load in forms
    wash_info = []
    heads_info = []
    hearts_info = []
    tails_info = []

    return render_template('day.html', wash=wash_info, heads=heads_info, hearts=hearts_info, tails=tails_info)


@app.route('/day/add_wash', methods=["POST"])
def add_wash():
    pass



if __name__ =='__main__':
    app.run(debug=True)