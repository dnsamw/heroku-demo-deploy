from flask import Flask, send_from_directory
from threading import Thread
import os


app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.png')


@app.route('/')
@app.route('/home')
def home():
    return "I'm alive"


# def run():
#     #app.run(host='localhost', port=8080)
#     app.run(host='0.0.0.0', port=8080)


# def keep_alive():
#     t = Thread(target=run)
#     t.start()


if __name__ == '__main__':
    app.secret_key = "ItIsASecret"
    app.debug = True
    app.run()
