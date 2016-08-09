from flask import session, request, abort, jsonify
from flask.ext.classy import FlaskView

class BaseRoute(FlaskView):

    route_base = '/'

    @classmethod
    def get_route_base(cls):
        route_base = super(BaseRoute, cls).get_route_base()
        return route_base

class BaseAuthenticatedRoute(FlaskView):

    route_base = '/'

    @classmethod
    def get_route_base(cls):
        route_base = super(BaseRoute, cls).get_route_base()
        return route_base
