from apppri import app
from flask import render_template

menu = [{"title": "начало", "url": "index"},
        {"title": "Главная", "url": "main"},
        ]


@app.route('/')
@app.route('/index')
def index():
    best_pri = {'username': 'Макарцев'}

    return render_template('index.html', title='2022 Forever', user=best_pri)


@app.route('/main')
def main():
    return render_template('main.html', menu=menu, title= 'Главная')
