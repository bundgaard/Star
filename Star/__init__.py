from flask import Flask
from flask.ext.pymongo import PyMongo
import itsdangerousinterface
app = Flask(__name__)
app.secret_key = '\x9e\x1d\xf1\x1fb\x0c\xbf\xa9{\x96"t\x0f\xe0A`\xd1\x9c\xb8\xba&b\xc6w\x13\xf3\xd8\xb8\x8c\xca\x17\x97'
app.config['MONGO1_DBNAME'] = 'users'
#app.session_interface = itsdangerousinterface.ItsdangerousSessionInterface()
mongo = PyMongo(app)
users = PyMongo(app, config_prefix='MONGO1')

import Star.views
from Star.api import api
from Star.admin import admin

app.register_blueprint(api, url_prefix='/api/v1')
app.register_blueprint(admin, url_prefix='/admin')
