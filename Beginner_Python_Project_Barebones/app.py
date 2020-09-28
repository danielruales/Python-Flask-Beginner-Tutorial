from flask import Flask, render_template, request, send_from_directory
from flask_material import Material
import os

app = Flask(__name__)
Material(app)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()