from flask import Flask
from  appist.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from appist import routes
