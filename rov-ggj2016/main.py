import os

#import logging
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from gamecontroller import GameController
import jsonpickle

############################
################### Init
############################

app = Flask(__name__)
socketio = SocketIO(app)
#print("starting up server")

app.config.from_pyfile('flaskapp.cfg')

#app.logger.debug('starting up server LOGGER')

gamecontroller = GameController()


############################
################### Routes
############################

@app.route("/")
def index():
    #return "Hello World!"
    return render_template('index.html')

@app.route("/siodemo")
def siodemo():
    #return "Hello World!"
    return render_template('siodemo.html')

@app.route("/client")
def client():
    #return "Hello World!"
    return render_template('client.html')

@app.route("/board")
def board():
    #return "Hello World!"
    return render_template('board.html')

# @app.route('/<path:resource>')
# def serveStaticResource(resource):
#    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

############################
################### Events
############################

################### General

@socketio.on('my event')
def handle_my_custom_event(json):
    print('Demo Event: ' + str(json))

'''
@socketio.on('disconnect')
def test_disconnect():
    print 'Something disconnected', request.sid
'''

################### Board

@socketio.on('connect', namespace='/board')
def handle_board_connected_event():
    print('Board Connected:', request.remote_addr)

@socketio.on('disconnect', namespace='/board')
def test_disconnect():
    print 'Board disconnected', request.remote_addr

@socketio.on("board reset", namespace='/board')
def handle_board_reset_event():
    print "Board will be reseted"
    gamecontroller.reset_game_state()
    all_players = jsonpickle.encode(gamecontroller.players,unpicklable=False)
    update_board_event('update players', all_players)

def update_board_event(event, data):
    print "Board event:", event, data
    socketio.emit(event, data, namespace='/board')

################### Client

@socketio.on('connect', namespace='/client')
def handle_client_connect_event():
    print 'Client Connected:', request.sid
    result = gamecontroller.add_player(request.sid)
    emit("player create result", jsonpickle.encode(result,unpicklable=False))
    all_players = jsonpickle.encode(gamecontroller.players,unpicklable=False)
    update_board_event('update players', all_players)

@socketio.on('disconnect', namespace='/client')
def handle_client_disconnected_event():
    print 'Client disconnected', request.sid
    gamecontroller.remove_player(request.sid)

@socketio.on("choose tile", namespace='/client')
def handle_tile_requested_event(data):
    print "event: choose tile", str(data['tile'])
    result = gamecontroller.request_tile(data['tile'], request.sid)
    result_json = jsonpickle.encode(result,unpicklable=False)
    emit("choose tile result", result_json)
    update_board_event('tile update',result_json)
    all_tiles = jsonpickle.encode(gamecontroller.board.tiles,unpicklable=False)
    update_board_event('tiles update',all_tiles)

@socketio.on("resolve tile", namespace='/client')
def handle_tile_resolve_event():
    result = gamecontroller.resolve_tile(request.sid)
    result_json = jsonpickle.encode(result,unpicklable=False)
    emit("resolve tile result", result_json)
    all_tiles = jsonpickle.encode(gamecontroller.board.tiles,unpicklable=False)
    update_board_event('tiles update',all_tiles)

@socketio.on('button pushed', namespace='/client')
def handle_button_pushed_event(json):
    print('Button pushed: ' + str(json))
    emit('button pushed', {'data': "Button was pushed by player " + request.sid}, broadcast=True)

############################
################### Run
###########################

port = int(os.environ.get('ROVPORT',8080))

if __name__ == '__main__':

    socketio.run(app,'0.0.0.0',port)
