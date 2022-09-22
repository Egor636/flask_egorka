from apppri import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    best_pri = {'username': 'Макарцев'}

    return render_template('indexpi.html', title='2022 Forever', user=best_pri)
