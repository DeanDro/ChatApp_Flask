from flask import Flask, render_template, session

from flask_socketio import SocketIO


app = Flask(__name__)

app.secret_key = 'thesuperultimatesecretkey'

socketio = SocketIO(app)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'mainUser',
                          'password': 'mainUserPassword',
                          'database': 'chatApp'
                          }


# main login page
@app.route('/')
def home_page():
    return render_template('frontend/login.html')


@app.route('/chatrooms', methods=['GET', 'POST'])
def chatrooms():
    return render_template('frontend/chatWindow.html')


def ack():
    print('message received')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received json:' +str(json))
    socketio.emit('Connected', broadcast=True, callback=ack)


if __name__ == '__main__':
    socketio.run(app, debug=True)
