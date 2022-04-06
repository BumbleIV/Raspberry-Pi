from flask import Flask, render_template, request, Response, redirect, url_for
from flask_socketio import SocketIO, emit


app = Flask(__name__)

app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO(app)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['blog_title']
        post = request.form['blog_main']
        post_entry = models.BlogPost(date=date, title=title, post=post)
        db.session.add(post_entry)
        db.session.commit()
        return redirect(url_for('database'))
    else:
        return render_template('./index.html')


def messageRecived():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
