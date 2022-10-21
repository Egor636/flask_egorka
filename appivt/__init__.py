from flask import Flask
from appivt.config import Config

app = Flask(__name__)

app.config.from_object(Config)

from appivt import routes
