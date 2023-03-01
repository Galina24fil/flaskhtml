from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/table/<n>/<age>')
def table(n, age):
    return render_template('table.html', n=n, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')