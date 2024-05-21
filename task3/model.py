from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # инициализируем БД


class User(db.Model):  # создаем модель для юзера
    id = db.Column(db.Integer, primary_key=True)  # первичный ключ
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
