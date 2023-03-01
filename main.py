from flask import Flask, render_template, request, url_for
import json
from random import randint
app = Flask(__name__)

@app.route('/member')
def member():
    with open('templates/member.json', encoding='utf-8') as file:
        s = json.load(file)
    a = randint(0, 2)
    return render_template('member.html', s=s, a=a)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')