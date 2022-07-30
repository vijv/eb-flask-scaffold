from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return "Flask with CICD"

@app.route('/value/<val>')
def printValue(val):
    val_d = {'value': val}
    return jsonify(val_d)

if __name__ == '__main__':
    app.debug = True
    app.run()
