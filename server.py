from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json
import pandas as pd
from Main import thisIsAFunction

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('sendData')
def handle_send_data(data):
    try:
        print(type(data))
        print('aaaaaaaaaaaaaaaaa')
        a = json.loads(data)
        print('qwqwqwwqwqwqwqwqw')
        print('Received data:', a)
        print('2252322656+56262626526')
        required_keys = ['N', 'P', 'K', 'moisture', 'temperature']
        print('79709098097986657656757587')
        print(a)
        print('nmnnnmnmnmnmnmnmmnmnmnmnm')
        w=a.pop(-1)
        for data in a:
            print(data)
            if any(key not in data for key in required_keys):
                print('-==-=-=-=-=-=-=-=--==-=-=====-=----===-')
                error_message = "Error: Missing N, P, K, moisture, or temperature in received data"
                print(error_message)
                print('qwsuahnuu')
                emit('response', json.dumps({"error": error_message}))
                return
        output = thisIsAFunction(a,w)
        response_json = output
        
        print("Response JSON:", response_json)
        emit('response', response_json)
    
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        emit('response', json.dumps({"error": error_message}))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3012)
