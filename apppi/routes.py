from apppi import app
from flask import render_template
from random import choice

menu = ['Главная', 'Помощь', 'О программе']

@app.route('/')
@app.route('/index')
def index():
    best_pi = {'username': 'Елизавета'}

    return render_template('index.html', title='2022 Forever', user=best_pi)


@app.route('/help')
def help():
    sp = ['PI', '2014', '']
    return render_template('help.html', title=choice(sp))


@app.route('/about')
def about():
    return render_template('about.html', menu=menu)
