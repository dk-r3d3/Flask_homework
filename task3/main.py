from flask import Flask, render_template, request, redirect, url_for
from model import User, db
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)  # инициализировали расширение SQLAlchemy
bcrypt = Bcrypt(app)  # для хеширования пароля


@app.route('/register', methods=['post', 'get'])
def register():
    if request.method == 'post':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        new_user = User(name=name, lastname=lastname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html')


@app.route('/success')
def success():
    return "Регистрация прошла успешно!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
