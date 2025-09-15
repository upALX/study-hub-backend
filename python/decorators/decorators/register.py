import functools
from flask import Flask, g, request, redirect, url_for

PLUGINS = []

def register(func):
    """Registra funcoes como plugins"""
    PLUGINS[func.__name__] = func
    return func

app = Flask(__name__)

def login_required(func):
    """Login required decorator to use the API"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...