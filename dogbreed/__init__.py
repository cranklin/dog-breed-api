from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.classy import FlaskView

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from dogbreed import routes, actions

# Configurations
app.config.from_object('config')

# Initiate models
from dogbreed.models import *
db.create_all()

# Flask error handling
from dogbreed.exceptions import *
# Generic 404 error handling
@app.errorhandler(404)
def not_found(error):
    # this requires a jinja template
    #return render_template('404.html'), 404
    return 'Not Found', 404

@app.errorhandler(NotAllowed)
def not_allowed(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(MalformedRequest)
def malformed_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
