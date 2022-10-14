from appist import app
from flask import render_template, request, flash, get_flashed_messages

menu = [{'name': 'Главная', 'url': 'index'}, {'name': 'Помощь', 'url': 'help'},
        {'name': 'Обратная связь', 'url': 'contact'}]


@app.route('/')
@app.route('/index')
def index():
    best_ist = {'username': 'Виктория'}
    favorite_writes = [{'author': {'username': 'Tolkien'},
                        'body': ' Lords of the ring'
                        },
                       {'author': {'username': 'Pushkin'},
                        'body': ' Capitans of the daughter'
                        },
                       {'author': {'username': 'Lermontov'},
                        'body': ' Парус'
                        }]

    return render_template('index.html', title='2022 Forever', menu=menu, user=best_ist,
                           favorite_writes=favorite_writes)


@app.route('/help')
def help():
    return render_template('help.html', title=' Помощь', menu=menu)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) >=2:
            flash('Сообщение отправлено', category='success')
            print(get_flashed_messages(True))
            print(request.form)
            print(request.form['username'])
        else:
            flash("Ошибка отправки", category='error')

    return render_template('contact.html', title=' Контакт', menu=menu)
