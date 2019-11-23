import flask_cors
from flask import (Flask, jsonify, request)

app = Flask(__name__)



if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    app.run(host="0.0.0.0")