from apppri import app
from flask import render_template, request, flash, session, redirect, url_for, abort

menu = [{"title": "Начало", "url": "index"},
        {"title": "Главная", "url": "main"},
        {"title": "Помощь", "url": "help"},
        {"title": "О приложении", "url": "about"},
        {"title": "Обратная связь", "url": "callback"},
        {"title": "Авторизация", "url": "login"}
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

@app.route('/profile/<username>')
def profile(username):
    if 'userlogged' not in session or  session['userlogged'] != username:
        abort(401)
    return f"<h1> Привет {username} </h1>"


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userlogged' in session:
        return redirect(url_for('profile', username=session['userlogged']))
    elif request.method == 'POST' and request.form['username'] == '1' and request.form['psw'] == '1':
        session['userlogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userlogged']))

    return render_template('login.html', title='Авторизация', menu=menu)


@app.errorhandler(404)
def page_404(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu, error=error)
