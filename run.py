from app import app
from flask_socketio import *

if __name__ == "__main__":
    socketio.run(app, debug=True)

    #app = socketio.Middleware(sio, app)
    #eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
