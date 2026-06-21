from flask import Flask
from flask import jsonify

from flask_cors import CORS

import analytics


app = Flask(__name__)

CORS(app)


# HOME
@app.route("/")
def home():

    return jsonify({

        "project":
        "ParkSense AI",

        "status":
        "Running",

        "routes": [

            "/summary",

            "/hotspots",

            "/hourly",

            "/vehicles",

            "/violations",

            "/stations",

            "/validation",

            "/geo",

            "/response-time"

        ]

    })


@app.route("/summary")
def summary():

    return jsonify(
        analytics.summary()
    )


@app.route("/hotspots")
def hotspots():

    return jsonify(
        analytics.hotspots()
    )


@app.route("/hourly")
def hourly():

    return jsonify(
        analytics.hourly()
    )


@app.route("/vehicles")
def vehicles():

    return jsonify(
        analytics.vehicles()
    )


@app.route("/violations")
def violation():

    return jsonify(
        analytics.violations()
    )


@app.route("/stations")
def station():

    return jsonify(
        analytics.stations()
    )


@app.route("/validation")
def validation():

    return jsonify(
        analytics.validation()
    )


@app.route("/geo")
def geo():

    return jsonify(
        analytics.geo()
    )


@app.route("/response-time")
def response():

    return jsonify(
        analytics.response_time()
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )