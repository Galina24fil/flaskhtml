from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index.html', title='Главная страница')

@app.route('/index/<username>')
def index(username):
    return render_template('index.html', title=username)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
