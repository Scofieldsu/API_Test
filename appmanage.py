# encoding: utf-8

from flask import Flask
from flaskapi.common import api
from flask_cors import *

import config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api.as_blueprint())
    # 跨域请求
    CORS(app, supports_credentials=True)
    app.config['DEBUG'] = config.DEBUG

    return app