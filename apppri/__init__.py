from flask import Flask
from apppri.config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'ikljsdehgfno;slkefjhgwielkjtnmgfwoiehjnewrkgn'


app.config.from_object(Config)

from apppri import routes
