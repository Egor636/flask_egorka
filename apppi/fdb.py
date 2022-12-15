import sqlite3


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
    pass


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def setMenu(self, title, url):
        try:
            self.__cur.execute('INSERT INTO mainmenu VALUES(NULL, ?, ?)', (title, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в БД', e)
            return False
        return True

    def delMenu(self, id=0):
        try:
            if id == 0:
                self.__cur.execute('DELETE FROM mainmenu')
            else:
                pass
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в БД', e)
            return False
        return True


if __name__ == '__main__':
    from apppi import app, connect_db
    db = connect_db()
    db = FDataBase(db)
    print(db.setMenu('Главная бд', 'about'))
    print(db.setMenu('Добавить статью', 'posts'))
    print(db.setMenu('Помощь', 'help'))
    print(db.setMenu('Главная', 'index'))
    print(db.setMenu('об авторе', 'me'))
    print(db.setMenu('Главное', 'base'))
    #print(db.delMenu())
    #create_db()


