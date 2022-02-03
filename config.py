import os

basedir = os.path.abspath(os.path.dirname(__file__))


class RunConfig(object):
    DEBUG = True
    SECRET_KEY = "secretkey"


class TestConfig(object):
    DEBUG = True
    SECRET_KEY = "secretkey"
