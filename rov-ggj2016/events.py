"""Events"""
from flask_socketio import SocketIO, send, emit
from main import socketio

############################
################### Events
############################

print "EVENTS!!!"

@socketio.on('client connected')
def handle_client_connected_event(json):
    print('Client Connected: ' + str(json))

@socketio.on('board connected')
def handle_client_connected_event(json):
    print('Board Connected: ' + str(json))

@socketio.on('button pushed')
def handle_button_pushed_event(json):
    print('Button pushed: ' + str(json))
    emit('button pushed', {'data': "Button was pushed!"}, broadcast=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    print('Demo Event: ' + str(json))

@socketio.on("Tile requested")
def handle_my_custom_event(json):
	print("Tile requested" + str(json))



