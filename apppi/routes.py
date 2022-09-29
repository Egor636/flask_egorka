from apppi import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    best_pi = {'username': 'Елизавета'}

    return render_template('index.html', title='2022 Forever', user=best_pi)


@app.route('/help')
def help():
    return render_template('help.html')
