from appivt import app
from flask import render_template


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

    return render_template('index.html', title='2022 Forever', user=best_ist, favorite_writes=favorite_writes)
