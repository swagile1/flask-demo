from flask import (Flask, Response, render_template, request, send_file)
from os import (getpid, kill)
from signal import SIGINT
from time import sleep
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import sys
from uuid import uuid4

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return '<h3>This is an example web application.</h3>'

@app.route('/users')
def users():
    conn = get_db_connection()
    users = conn.execute('SELECT created, name, location FROM users;').fetchall()
    conn.close()
    return render_template('users.html', users=users)

@app.route('/greet/<person>')
def greet(person):
    return f'<h1>Hello, {person}!</h1>'

@app.route('/caption', methods=['POST'])
def caption():
    caption = request.form.get('caption')

    filename = create_captioned_file(caption)
    return render_template('pickles.html', filename=filename, caption=caption)

def create_captioned_file(caption):
    try:
        pickles = Image.open("images/pickles-raindrop.jpg")

    except:
        print("Unable to load image")
        sys.exit(1)

    idraw = ImageDraw.Draw(pickles)
    text = caption

    font = ImageFont.truetype("fonts/LiberationSerif-Regular.ttf", size=18)

    idraw.text((10, 10), text, font=font)
    filename = 'images/' + uuid4().hex + '.png'
    pickles.save(filename)
    return filename

@app.route('/images/<file>')
def images(file):
    return send_file('images/' + file)

@app.get('/shutdown')
def shutdown():
    response = Response('<h1>Server shutting down...</h1>')

    @response.call_on_close
    def on_close():
        sleep(2)
        kill(getpid(), SIGINT)

    return response
