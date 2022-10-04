from apppri import app
from flask import render_template

menu = [{"title": "Начало", "url": "index"},
        {"title": "Главная", "url": "main"},
        {"title": "Помощь", "url": "help"},
        {"title": "О приложении", "url": "about"},
        ]


@app.route('/')
@app.route('/index')
def index():
    best_pri = {'username': 'Макарцев'}

    return render_template('index.html', title='2022 Forever', user=best_pri)


@app.route('/help')
def help():
    return render_template('help.html', title='Помощь', menu=menu)


@app.route('/about')
def about():
    return render_template('help.html', title='C горем попалам ПРИ', menu=menu)



@app.route('/main')
def main():
    return render_template('main.html', menu=menu, title='Главная')
