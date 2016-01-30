"""Events"""

############################
################### Events
############################

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