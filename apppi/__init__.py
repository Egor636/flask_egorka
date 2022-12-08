import os

from flask import Flask

from apppi.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flask_db.db')))

from apppi import routes
