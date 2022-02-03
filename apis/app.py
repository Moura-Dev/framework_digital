from flask import Flask, request
from flasgger import Swagger
from apis.api import framework_blueprint


def create_app(app_name="framework", test_config=False, production_conf=False):
    app = Flask(app_name)
    swagger = Swagger(app)
    if test_config:
        app.config.from_object("config.TestConfig")
    else:
        app.config.from_object("config.RunConfig")

    app.register_blueprint(framework_blueprint)
    import error_handlers

    return app
