from flask import Flask
from flask import jsonify

application = Flask(__name__)

@application.route('/')
def main():
    return "Hello! Testing CD"

@application.route('/value/<val>')
def printValue(val):
    val_d = {'value': val}
    return jsonify(val_d)

if __name__ == '__main__':
    application.debug = True
    application.run()
