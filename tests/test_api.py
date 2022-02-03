import os
import sys
from base64 import b64encode

import pytest
import requests
from flask.testing import FlaskClient

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from apis.app import create_app


@pytest.fixture(scope="module")
def app():
    app = create_app(test_config=True)

    yield app


@pytest.fixture(scope='module')
def flask_app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture(scope='module')
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    return app.test_client()

def test_json_place_holder():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    assert response.status_code == 200
    assert response.reason == "OK"


def test_index(client):
    credentials = b64encode(b"framework_digital:secret").decode('utf-8')
    response_login = client.get("/login/", headers={"Authorization": f"Basic {credentials}"})
    token = response_login.json['token']
    response = client.get("/", headers={"Authorization": f"Bearer {token}"})
    data = response.json
    assert data[0]['title'] == 'delectus aut autem'
    assert data[0]['id'] == 1
    assert response.status == "200 OK"
    assert response.status_code == 200


def test_index_missing_token(client):
    token = ''
    response = client.get("/", headers={"Authorization": f"Bearer {token}"})
    data = response.json
    assert data['message'] == 'Token is missing!'
    assert response.status == "403 FORBIDDEN"
    assert response.status_code == 403


def test_index_invalid_token(client):
    token = 'aaaaaaaaaaaaaaa'
    response = client.get("/", headers={"Authorization": f"Bearer {token}"})
    data = response.json
    assert data['message'] == 'Token is invalid!'
    assert response.status == "403 FORBIDDEN"
    assert response.status_code == 403


def test_login(client):
    credentials = b64encode(b"framework_digital:secret").decode('utf-8')
    response = client.get("/login/", headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200
    assert response.status == "200 OK"


def test_login_fail(client):

    credentials = b64encode(b"secret:secret").decode('utf-8')
    response = client.get("/login/", headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 401
    assert response.status == "401 UNAUTHORIZED"

