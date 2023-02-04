from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list_prof/<list>')
def index(list):
    if list == 'ol':
        return render_template('index.html', ol=1, ul=0)
    if list == 'ul':
        return render_template('index.html', ul=1, ol=0)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')