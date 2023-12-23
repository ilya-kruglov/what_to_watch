from datetime import datetime
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


class Opinion(db.Model):
    # ID — целое число, первичный ключ
    id = db.Column(db.Integer, primary_key=True)
    # Название фильма — строка длиной 128 символов, не может быть пустым
    title = db.Column(db.String(128), nullable=False)
    # Мнение о фильме — большая строка, не может быть пустым,
    # должно быть уникальным
    text = db.Column(db.Text, unique=True, nullable=False)
    # Ссылка на сторонний источник — строка длиной 256 символов
    source = db.Column(db.String(256))
    # Дата и время — текущее время,
    # по этому столбцу база данных будет проиндексирована
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


@app.route('/')
def index_view():
    # pp(app.config)
    return 'Совсем скоро тут будет случайное мнение о фильме!'


if __name__ == '__main__':
    app.run()
