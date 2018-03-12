from flask import Flask, current_app, jsonify, request

import json
import codecs
import os

from api import api



def loadjson(app, filename):
    reader = codecs.getreader("utf-8")
    with app.open_resource(filename) as f:
        return json.load(reader(f))

def create_app(config=None):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__, root_path=APP_ROOT)
    app.debug = True
    app.config['SECRET_KEY'] = "\xcf\xa6\xe20P&\xd8\x86\xcf'\x863\x7f\xfb\xf9\x16\xd4\xf0\x9bj0\x07$`"
    app.config["people"] = loadjson(app,"./resources/people.json")
    app.config["companies"] = loadjson(app,"resources/companies.json")
    app.config.update(config or {})
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(api)






if __name__ == "__main__":
    app.run()
