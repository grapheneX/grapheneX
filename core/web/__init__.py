from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '77a98d7971ec94c8aae6dd2d'
socketio = SocketIO(app)

from core.web.views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    socketio.run(app)