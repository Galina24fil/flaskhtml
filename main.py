from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def index1():
    s = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('auto_answer.html', title='По каютам!', s=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')