from flask import Flask
from config import RunConfig

app = Flask(__name__)
app.config.from_object(RunConfig)