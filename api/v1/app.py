#!/usr/bin/python3
""" Module containing Flask application """
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ closes the storage """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """ Returns a JSON formatted 404 status code response """
    data = {
        'error': 'Not found'
    }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
