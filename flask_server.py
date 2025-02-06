from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)


def send_data():
    while True:
      
        float_data = [round(random.uniform(0, 100), 2) for _ in range(5)]
      
        socketio.emit('float_data', {'data': float_data})
      
        time.sleep(1)


@app.route('/')
def index():
   return  "hello"#render_template('index.html')


@app.before_first_request
def before_first_request():
    thread = threading.Thread(target=send_data)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
