from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # отображаем шаблон index.html


@app.route('/submit', methods=['POST'])  # обрабатывает post запрос по адресу /submit
def submit():
    name = request.form['name']  # получают значения из формы
    email = request.form['email']  # получают значения из формы

    resp = make_response(redirect('/welcome'))  # Создает HTTP-ответ с перенаправлением на /welcome
    resp.set_cookie('username', name)  # установка cookies
    resp.set_cookie('email', email)  # установка cookies
    return resp


@app.route('/welcome')
def welcome():
    username = request.cookies.get('username')
    if not username:
        return redirect('/')
    return render_template('welcome.html', username=username)


@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))  # перенаправление на главную страницу
    resp.delete_cookie('username')  # удаление cookies
    resp.delete_cookie('email')  # удаление cookies
    return resp


if __name__ == '__main__':
    app.run(debug=True)
