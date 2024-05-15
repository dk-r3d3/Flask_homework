from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/base/')
def base_html():
    return render_template('base.html')


@app.route('/close/')
def close_html():
    return render_template('close.html')


@app.route('/foot/')
def foot_html():
    return render_template('foot.html')


@app.route('/jaket/')
def jaket_html():
    return render_template('jaket.html')


if __name__ == '__main__':
    app.run(debug=True)
