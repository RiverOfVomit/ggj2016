from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

############################
################### Events
############################

@socketio.on('client connected')
def handle_client_connected_event(json):
    print('Client Connected: ' + str(json))
    gamecontroller.add_player(request.sid)

@socketio.on('board connected')
def handle_client_connected_event(json):
    print('Board Connected: ' + str(json))

@socketio.on('button pushed')
def handle_button_pushed_event(json):
    print('Button pushed: ' + str(json))
    emit('button pushed', {'data': "Button was pushed by player " + request.sid}, broadcast=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    print('Demo Event: ' + str(json))

@socketio.on("Tile requested")
def handle_tile_requested_event(json):
    print request.sid, type(request.sid)
    gamecontroller.request_tile(request.sid)

@socketio.on("choose tile")
def handle_tile_requested_event(data):
    print "event: choose tile", str(data['tile'])
    success = gamecontroller.request_tile(data['tile'], request.sid)
    emit("tile reserved",{'sucess': success})
