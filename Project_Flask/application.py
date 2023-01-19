from flask import Flask

# flask --app application.py --debug run

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1>Hello World</h1>"

@application.route('/usuarios')
def miNombre():
    return "<div>Enrique Perez</div>"

@application.route('/usuarios/<username>')
def return_username(username):
    return username


