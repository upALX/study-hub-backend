from flask import Flask, jsonify
from errors import base_errors

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return jsonify("Hello world!")


@app.route("/lol/")
def no_hello():
    return base_errors.ExceptionsFromApi(message='Hello', more_information='HERE', status_code=407, title='Tile')