from flask import Flask, render_template, request, Response, redirect, url_for
from flask_socketio import SocketIO, emit


app = Flask(__name__)

app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('./index.html')


def messageRecived():
    print('message was received!!!')


@socketio.on('My Event')
def handle_my_custom_event(json):
    print('Received' + str(json))
    socketio.emit('My Response', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
