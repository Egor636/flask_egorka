from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'ываываыва<h1>Мое первое приложение на фласке!!</h1> <p> Вторая строчка </p>' \
           '<table><table border=#><tr><td>ячейка 1</td><td>ячейка 2</td></tr></table> '


@app.route('/privet/')
def greeting():
    return '<h2> Здравствуй милый друг </h2>'


@app.route('/<user>/')
def users(user):
    return f'<h2> Здравствуй наш пользователь {user} </h2>'


@app.route('/<int:id>/')
def users_id(id):
    return f'<h2> Ваш номер после номера {id} </h2>'


if __name__ == '__main__':
    app.run(debug=True)
