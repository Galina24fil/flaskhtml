from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def index1():
    title = 'Анкета'
    surname = 'Watny'
    name = 'Mark'
    education = 'выше среднего'
    profession = 'штурман марсохода'
    sex = 'male'
    motivation = 'Всегда мечтал застрять на Марсе!'
    ready = 'True'
    s = {'Фамилия': surname, 'Имя': name, 'Образование': education, 'Профессия': profession,
         'Пол': sex, 'Мотивация': motivation, 'Готовы остаться на Марсе?': ready}
    return render_template('auto_answer.html', title=title, s=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
