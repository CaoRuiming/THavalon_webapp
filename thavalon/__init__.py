from flask import Flask, render_template
from flask_migrate import Migrate
import logging.config
import os
import json
from .webpack import init_webpack
from .models import db
from .controllers.test import test_controller

with open(os.path.join(os.path.dirname(__file__), 'logging.json')) as f:
    config = json.load(f)
    logging.config.dictConfig(config)

app = Flask(__name__)
app.config.from_object('thavalon.settings')

init_webpack(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(test_controller, url_prefix='/')

import logging

log = logging.getLogger(__name__)
log.info('Started THavalon...')
