from flask import Blueprint,render_template

base= Blueprint('base', __name__)

@base.route('/')
def home():

    return render_template("base.html")