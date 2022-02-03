from functools import wraps
import jwt
from flask import current_app, jsonify, request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("authorization")
        token = ""
        if auth:
            token = auth.replace("Bearer", "").strip()

        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )

        except:
            return jsonify({"message": "Token is invalid!"}), 403

        return f(*args, **kwargs)

    return decorated
