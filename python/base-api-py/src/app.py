from flask import Flask, jsonify
from .errors import ExceptionsFromApi

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return jsonify("Hello world!")


@app.route("/lol/")
def no_hello():
    return ExceptionsFromApi(message='Hello', more_information='HERE', status_code=407, title='Title')