import datetime
import logging

import jwt
import requests
from flask import Blueprint, current_app, jsonify, request, make_response

from decorator import token_required

framework_blueprint = Blueprint("framework", __name__)


@framework_blueprint.route("/", methods=["GET"])
@token_required
def framework_request():
    """Checks if the system is alive
    ---
    responses:
      200:
        description: OK if the system is alive
    """
    try:
        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url=url)
        response_json = response.json()
        if response_json:
            lista = response_json[:5]
            new_list = [{"id": d["id"], "title": d["title"]} for d in lista]
        logging.basicConfig(filename="sucess.log", level=logging.DEBUG)
        logging.info(lista)

        return jsonify(new_list)

    except:
        logging.basicConfig(filename="error.log", level=logging.DEBUG)
        logging.error("Exception occurred", exc_info=True)
        return {"reason": "error description"}


@framework_blueprint.route("/login/", methods=["GET"])
def login():
    auth = request.authorization

    if auth and auth.username == "framework_digital" and auth.password == "secret":
        token = jwt.encode(
            {
                "user": auth.username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return make_response({"token": token})

    return make_response(
        "Nao foi possivel verificar!",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )
