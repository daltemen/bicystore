import logging

from flask import Flask, render_template, request, jsonify, abort

from backends.models_controller import ModelController

app = Flask(__name__)


@app.route('/bicystore/api/v1/bicycles/<int:bicycle_id>', methods=['GET', 'PUT', 'DELETE'])
def bicycles(bicycle_id):
    bicycle = ModelController.get_model_by_slug_name('bicycle')
    bicycle = bicycle.get_by_id(int(bicycle_id))
    if bicycle is not None:
        if request.method == 'GET':
            return jsonify({
                'bicycle': {
                    'id': bicycle.key.id(),
                    'wheels': bicycle.wheels,
                    'saddle': bicycle.saddle,
                    'frame': bicycle.frame,
                    'chain': bicycle.chain,
                    'fork': bicycle.fork,
                    'brakes': bicycle.brakes
                }
            })
        elif request.method == 'PUT':
            import pdb; pdb.set_trace()
            bicycle = ModelController.get_model_for_update(model_name='bicycle', request_dict=request.json)
            # TODO: Do PUT method
            return jsonify({
                'bicycle': {
                    'id': bicycle.key.id(),
                    'wheels': bicycle.wheels,
                    'saddle': bicycle.saddle,
                    'frame': bicycle.frame,
                    'chain': bicycle.chain,
                    'fork': bicycle.fork,
                    'brakes': bicycle.brakes
                }
            })
        elif request.method == 'DELETE':
            bicycle.delete()
            return jsonify({
                'message': 'successful'
            })
        else:
            return abort(400)

    return jsonify({'bicycle': {}})


@app.route('/bicystore/api/v1/bicycles', methods=['POST'])
def post_bicycle():
    bicycle = ModelController.get_model_for_creation(model_name='bicycle', request_dict=request.json)
    if bicycle is None:
        abort(400)
    bicycle.put()
    return jsonify({
        'bicycle': {
            'id': bicycle.key.id(),
            'wheels': bicycle.wheels[0].key.id() if bicycle.wheels else None,
            'saddle': bicycle.saddle[0].key.id() if bicycle.saddle else None,
            'frame': bicycle.frame[0].key.id() if bicycle.frame else None,
            'chain': bicycle.chain[0].key.id() if bicycle.chain else None,
            'fork': bicycle.fork[0].key.id() if bicycle.fork else None,
            'brakes': bicycle.brakes[0].key.id() if bicycle.brakes else None,
        }
    })


@app.route('/bicystore/api/v1/wheels', methods=['GET', 'POST'])
def wheels():
    wheel = ModelController.get_model_by_slug_name('wheel')
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        wheel.name = request.json['name']
        wheel.put()
        return jsonify({
            'wheel': {
                'id': wheel.key.id(),
                'name': wheel.name
            }
        })
    else:
        query = wheel.query()
        results = list(query.fetch())
        return jsonify({
            'wheels': [{
                'id': w.key.id(),
                'name': w.name
            } for w in results]
        })


@app.route('/bicystore/api/v1/saddles', methods=['GET', 'POST'])
def saddles():
    saddle = ModelController.get_model_by_slug_name('saddle')
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        saddle.name = request.json['name']
        saddle.put()
        return jsonify({
            'saddle': {
                'id': saddle.key.id(),
                'name': saddle.name
            }
        })
    else:
        query = saddle.query()
        results = list(query.fetch())
        return jsonify({
            'saddles': [{
                'id': s.key.id(),
                'name': s.name
            } for s in results]
        })


@app.route('/bicystore/api/v1/frames', methods=['GET', 'POST'])
def get_frames():
    frame = ModelController.get_model_by_slug_name('frame')
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        frame.name = request.json['name']
        frame.put()
        return jsonify({
            'frames': {
                'id': frame.key.id(),
                'name': frame.name
            }
        })
    else:
        query = frame.query()
        results = list(query.fetch())
        return jsonify({
            'frames': [{
                'id': f.key.id(),
                'name': f.name
            } for f in results]
        })


@app.route('/bicystore/api/v1/chains', methods=['GET', 'POST'])
def chains():
    chain = ModelController.get_model_by_slug_name('chain')
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        chain.name = request.json['name']
        chain.put()
        return jsonify({
            'chain': {
                'id': chain.key.id(),
                'name': chain.name
            }
        })
    else:
        query = chain.query()
        results = list(query.fetch())
        return jsonify({
            'chains': [{
                'id': c.key.id(),
                'name': c.name
            } for c in results]
        })


@app.route('/bicystore/api/v1/forks', methods=['GET', 'POST'])
def forks():
    fork = ModelController.get_model_by_slug_name('fork')
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        fork.name = request.json['name']
        fork.put()
        return jsonify({
            'fork': {
                'id': fork.key.id(),
                'name': fork.name
            }
        })
    else:
        query = fork.query()
        results = list(query.fetch())
        return jsonify({
            'forks': [{
                'id': f.key.id(),
                'name': f.name
            } for f in results]
        })


@app.route('/bicystore/api/v1/brakes', methods=['GET', 'POST'])
def brakes():
    brake = ModelController.get_model_by_slug_name('brake')
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        brake.name = request.json['name']
        brake.put()
        return jsonify({
            'brake': {
                'id': brake.key.id(),
                'name': brake.name
            }
        })
    else:
        query = brake.query()
        results = list(query.fetch())
        return jsonify({
            'brakes': [{
                'id': b.key.id(),
                'name': b.name
            } for b in results]
        })


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
