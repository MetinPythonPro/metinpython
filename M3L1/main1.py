from flask import Flask
import random
import requests

app = Flask(__name__)

facts_list = ["The Earth is round!", "The Sun is round!", "The Moon is round!", "You are human!", "You are using a device!"]

@app.route("/")
def main_page():
    return '<h1 style = "color: #FF7B19; font-size: 100px;">click them!</h1><a style = "color: #2200CC; font-size: 100px;" href="/random_truths">CLİCK  ME!!!</a><br/><br/><a style = "color: #2200CC; font-size: 100px;" href="/random_dog">NO!!!  CLİCK ME!!!</a>'

@app.route("/random_truths")
def click_me():
    return f'<p style = "color: #ACE1AF; font-size: 100px;">{random.choice(facts_list)}</p>'

@app.route("/random_dog")
def  no_me():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return f"<img src = {data['url']}>"

app.run(debug=True)