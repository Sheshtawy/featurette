from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import settings

env = settings.get_env()

app = Flask(__name__)
app.config.from_pyfile(env)

db = SQLAlchemy(app)
