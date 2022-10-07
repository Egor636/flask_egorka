from appivt import app
from flask import render_template, request

menu = [{'name': 'Главная', 'url': 'index'}, {'name': 'Блюда', 'url': 'dishes'}, {'name': 'Помощь', 'url': 'help'},
        {'name': 'Контакт', 'url': 'contact'}]

bd_contact = []


@app.route('/')
@app.route('/index')
def index():
    best_ivt = {'username': 'Шляпкин'}
    favorite_writes = [{'author': {'username': 'Tolkien'},
                        'body': ' Lords of the ring'
                        },
                       {'author': {'username': 'Pushkin'},
                        'body': ' Capitans of the daughter'
                        },
                       {'author': {'username': 'Lermontov'},
                        'body': ' Парус'
                        }]

    return render_template('index.html', title='2022 Forever', user=best_ivt, favorite_writes=favorite_writes,
                           menu=menu)


@app.route('/dishes')
def dish():
    best_user = {'username': 'Николай'}
    favorite_dishes = [{'name': {'dishname': 'Fried chicken'},
                        'ingridients': {'ingr1': 'Meat of chicken',
                                        'ingr2': 'some spicy sauce'},
                        'photo': 'https://hi-news.ru/wp-content/uploads/2020/06/chicken_home_image_one-750x558.jpg'}]

    return render_template('dishes.html', title='2022 Forever', abuser=best_user, favorite_dishes=favorite_dishes,
                           menu=menu)


@app.route('/help')
def help():
    return render_template('help.html', title='Cправка', menu=menu)


def rec(bd, f):
    print(f['username'])
    bd.append({'username': f['username'], 'message': f['message']})

@ app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        rec(bd_contact, request.form)
        print(request.form['username'])

        print(bd_contact)

    return render_template('contact.html', title='Контакты', menu=menu)
