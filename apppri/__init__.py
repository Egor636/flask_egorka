from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ikljsdehgfno;slkefjhgwielkjtnmgfwoiehjnewrkgn'

from apppri import routes
