from apppri import app
from flask import render_template, request, flash

menu = [{"title": "Начало", "url": "index"},
        {"title": "Главная", "url": "main"},
        {"title": "Помощь", "url": "help"},
        {"title": "О приложении", "url": "about"},
        {"title": "Обратная связь", "url": "callback"}
        ]


@app.route('/')
@app.route('/index')
def index():
    best_pri = {'username': 'Макарцев'}

    return render_template('index.html', title='2022 Forever', menu=menu, user=best_pri)


@app.route('/help')
def help():
    return render_template('help.html', title='Помощь', menu=menu)


@app.route('/about')
def about():
    return render_template('help.html', title='C горем попалам ПРИ', menu=menu)


@app.route('/main')
def main():
    return render_template('main.html', menu=menu, title='Главная')


@app.route('/callback', methods=["POST", "GET"])
def callback():
    if request.method == 'POST':
        if len(request.form['username']) > 2 and '@' in request.form['email']:
            flash('Сообщение отправлено', category='success')
        else:
            flash('  Ошибка отправки', category='error')
        print(request.form)
        print(request.form['email'])
    return render_template('callback.html', menu=menu, title="Обратная связь")
