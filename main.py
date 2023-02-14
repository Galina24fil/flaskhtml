from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('index.html', prof=1)
    else:
        return render_template('index.html', prof=0)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
