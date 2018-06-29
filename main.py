import logging

from flask import Flask, render_template, request, jsonify

from models.mock_data import MOCK_PART

app = Flask(__name__)


@app.route('/bicystore/api/v1/bicycles/<int:bicycle_id>', methods=['GET', 'PUT', 'DELETE'])
def bicycles(bicycle_id):
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/bicycle', methods=['POST'])
def post_bicycle():
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/wheels', methods=['GET'])
def get_wheels():
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/saddles', methods=['GET'])
def get_saddles():
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/frames', methods=['GET'])
def get_frames():
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/chains', methods=['GET'])
def get_chains():
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/forks', methods=['GET'])
def get_forks():
    return jsonify({'part': MOCK_PART})


@app.route('/bicystore/api/v1/brakes', methods=['GET'])
def get_brakes():
    return jsonify({'part': MOCK_PART})


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
