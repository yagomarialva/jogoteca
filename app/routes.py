from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Olá, Flask!"

@main.route('/inicio')
def ola():
    return render_template('./templates/lista.html')