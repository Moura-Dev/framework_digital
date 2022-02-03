from flask import jsonify

from apis.app import create_app

app = create_app()


@app.errorhandler(404)
def not_found(e):
    return jsonify({"Message": "Not Found"}, 404)


@app.errorhandler(500)
def internal_error(e):
    return jsonify({"Message": "Internal Error"}, 500)
