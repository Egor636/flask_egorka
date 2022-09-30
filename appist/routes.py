from appist import app
from flask import render_template

menu = ['Главная', 'Помощь']


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
