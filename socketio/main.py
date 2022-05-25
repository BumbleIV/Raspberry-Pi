from flask import Flask, render_template, request, Response, redirect, url_for
from flask_socketio import SocketIO, emit, send


app = Flask(__name__)

app.config['SECRET_KEY'] = 'so secret'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('./index.html')


def message_received():
    print('Message Received')


@socketio.on('My Event')
def handle_my_custom_event(json):
    print('Received' + str(json))
    socketio.emit('My Response', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(app, debug=True)
