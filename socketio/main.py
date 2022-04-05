from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)

# index route


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    socketio.run(app)



# button iteraction:
# use an html form to send a message to the server <form>
# look up hmtl form pattern
# wrap button in a form

# use javascript as an alternative to html form
