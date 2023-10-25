from flask import request

def register_blueprints(app):
    from src.routes.base import base_route

    app.register_blueprint(base_route)