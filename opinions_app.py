# from pprint import pprint as pp

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Подключается БД SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# Задаётся конкретное значение для конфигурационного ключа
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# В ORM передаётся в качестве параметра экземпляр приложения Flask
db = SQLAlchemy(app)


@app.route('/')
def index_view():
    # pp(app.config)
    return 'Совсем скоро тут будет случайное мнение о фильме!'


if __name__ == '__main__':
    app.run()
