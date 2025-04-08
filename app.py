from flask import Flask, render_template, request, redirect, url_for
import random
import string
import re

app = Flask(__name__)

# Room name generator
def generate_room_name():
    random_part = ''.join(random.choices(string.ascii_letters, k=6))
    return f"SV-{random_part}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create', methods=['POST'])
def create():
    room = generate_room_name()
    return redirect(url_for('index', room=room))

@app.route('/meeting/<room>')
def index(room):
    return render_template('index.html', room=room)

if __name__ == '__main__':
    app.run(debug=True)
