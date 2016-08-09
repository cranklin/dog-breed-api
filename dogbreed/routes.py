from dogbreed import app
from dogbreed.actions import Actions
from dogbreed.exceptions import *
from flask import Flask, jsonify, request, abort, render_template
import json

@app.route('/')
@app.route('/index')
@app.route('/api')
def index():
    ret = render_template(
        'index.html',
        endpoints = [
            {
                'title': 'Show all dogs',
                'url': '/api/dogs or /api/dogs?order_by=breed or /api/dogs?order_by=votes',
                'method': 'GET',
                'url_params': 'Optional: order_by=[breed | votes]',
                'data_params': None,
                'success_response': '''
                    Example:
                    Code: 200
                    Content:
                    [
                        {
                            "votes": {
                                "dog_id": 10,
                                "counter": 2,
                                "dog": null
                            },
                            "date_modified": null,
                            "breed": {
                                "id": 1,
                                "date_created": null,
                                "dogs": null,
                                "breed_name": "labrador",
                                "date_modified": null
                            },
                            "dog_description": null,
                            "breed_id": 1,
                            "date_created": null,
                            "dog_name": null,
                            "id": 10,
                            "photo_url": "http://i.imgur.com/kSU7Zca.png"
                        },
                        ...
                    ]
                ''',
                'error_response': None,
                'sample_call': None,
                'notes': None
            },
            {
                'title': 'Show dog',
                'url': '/api/dogs/:id',
                'method': 'GET',
                'url_params': 'Required: id=[integer]',
                'data_params': None,
                'success_response': '''
                    Example:
                    Code: 200
                    Content:
                    {
                        "votes": {
                            "dog_id": 10,
                            "counter": 2,
                            "dog": null
                        },
                        "date_modified": null,
                        "breed": {
                            "id": 1,
                            "date_created": null,
                            "dogs": null,
                            "breed_name": "labrador",
                            "date_modified": null
                        },
                        "dog_description": null,
                        "breed_id": 1,
                        "date_created": null,
                        "dog_name": null,
                        "id": 10,
                        "photo_url": "http://i.imgur.com/kSU7Zca.png"
                    }
                ''',
                'error_response': None,
                'sample_call': None,
                'notes': None
            },
            {
                'title': 'Show all breeds',
                'url': '/api/breeds',
                'method': 'GET',
                'url_params': None,
                'data_params': None,
                'success_response': '''
                    Example:
                    Code: 200
                    Content:
                    [
                        {
                            "id": 1,
                            "date_created": null,
                            "dogs": null,
                            "breed_name": "labrador",
                            "date_modified": null
                        },
                        ...
                    ]
                ''',
                'error_response': None,
                'sample_call': None,
                'notes': None
            },
            {
                'title': 'Show dogs by breed',
                'url': '/api/breeds/:id',
                'method': 'GET',
                'url_params': 'Required: id=[integer]',
                'data_params': None,
                'success_response': '''
                    Example:
                    Code: 200
                    Content:
                    [
                        {
                            "votes": {
                                "dog_id": 10,
                                "counter": 2,
                                "dog": null
                            },
                            "date_modified": null,
                            "breed": {
                                "id": 1,
                                "date_created": null,
                                "dogs": null,
                                "breed_name": "labrador",
                                "date_modified": null
                            },
                            "dog_description": null,
                            "breed_id": 1,
                            "date_created": null,
                            "dog_name": null,
                            "id": 10,
                            "photo_url": "http://i.imgur.com/kSU7Zca.png"
                        },
                        ...
                    ]
                ''',
                'error_response': None,
                'sample_call': None,
                'notes': None
            },
            {
                'title': 'Vote for dog',
                'url': '/api/dogs/vote',
                'method': 'POST',
                'url_params': None,
                'data_params': "{'dog': [integer]}",
                'success_response': '''
                    Example:
                    Code: 201
                    Content:
                    {
                        "vote": 99
                    },
                ''',
                'error_response': '''
                    Code: 403
                    Content:
                    {
                        "message": "User already voted"
                    }

                    OR

                    Code: 400
                    Content:
                    {
                        "message": "Required parameter(s) missing: dog"
                    }
                ''',
                'sample_call': None,
                'notes': None
            }
        ]
    )
    return ret

@app.route('/api/dogs')
def get_all_dogs():
    order_by = request.args.get('order_by', None)
    dogs = Actions.get_all_dogs(order_by=order_by)
    return json.dumps(dogs)

@app.route('/api/dogs/<dog_id>')
def get_dog(dog_id):
    dog = Actions.get_dog(dog_id)
    return json.dumps(dog)

@app.route('/api/breeds')
def get_all_dog_breeds():
    breeds = Actions.get_all_breeds()
    return json.dumps(breeds)

@app.route('/api/breeds/<breed_id>')
def get_all_breed(breed_id):
    dogs = Actions.get_all_dogs_by_breed(breed_id)
    return json.dumps(dogs)

@app.route('/api/dogs/vote', methods=['POST'])
def post_dog_vote():
    if not request.json or not request.json.has_key('dog'):
        # 'dog' is not found in POST data.
        raise MalformedRequest("Required parameter(s) missing: dog")
    dog_id = request.json.get('dog')
    agent = request.headers.get('User-Agent')
    response = Actions.submit_dog_vote(dog_id, agent)
    return jsonify(response), 201
