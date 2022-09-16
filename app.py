from flask import Flask, render_template
from random import choice

app = Flask(__name__)


@app.route('/')
def hello():
    return 'БГИТУ лучшие'


@app.route('/ist/')
def hello_ist():
    user = {'username': 'Cтанислав'}
    title_sp = ("Олень", 'Деноминация', 'Феррари')
    return render_template('index.html', title=choice(title_sp), user=user)


@app.route('/ivt/')
def hello_ivt():
    ivt_losers = {'1': ('Нестеренко',
                        'https://s9.travelask.ru/uploads/post/000/007/248/main_image/facebook-ac0e57a43e3c6ebd9d8e072f7bceb986.jpg'),
                  '2': ('Мотора',
                        'https://brothers-smaller.ru/wp-content/uploads/2015/11/110815_1224_1.jpg'),
                  '3': ('Медведев',
                        'https://img.kanal-o.ru/img/2018-08-06/fmt_81_24_shutterstock_688280269.jpg')}
    ivt_winners = {'1': ('Шляпкин',
                         'https://usatiki.ru/wp-content/uploads/2017/08/dikaya-sobaka-dingo.jpg'),
                   '2': ('Шипик',
                         'https://n1s1.hsmedia.ru/58/b3/be/58b3beebf187d6aba5c3e6fd3e2db858/1920x1152_0xac120003_11540205301626197607.jpg'),
                   '3': ('Рябцев',
                         'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTm1kuf0UttkM8diwtGA42b_1U7Sh7giKDtFg&usqp=CAU')}

    title_r = ('Будущее группы ИВТ', 'Хребет ИВТ')
    # title_sp = ("Олень", 'Деноминация', 'Феррари')
    # return render_template('index.html', title=choice(title_sp),  user=user)
    return render_template('ivt.html', title=choice(title_r), user=choice(list(ivt_losers.items())),
                           user_otl=choice(list(ivt_winners.items())))


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
