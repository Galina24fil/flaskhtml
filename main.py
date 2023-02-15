from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h3>для участия в миссии</h3>
                            <div>
                                <form class="login_form" method ="post">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label> 
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        a = request.form['file']
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Отбор астронавтов</title>
                                  </head>
                                  <body>
                                    <h1>Загрузка фотографии</h1>
                                    <h3>для участия в миссии</h3>
                                    <div>
                                        <form class="login_form" method ="post">
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label> 
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            </br>
                                            <img src="/static/{a}" class="d-block w-100" alt="Картинка не открылась...">
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')