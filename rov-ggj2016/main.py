import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from gamecontroller import GameController


############################
################### Init
############################

app = Flask(__name__)
socketio = SocketIO(app)
print("starting up server")

app.config.from_pyfile('flaskapp.cfg')

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

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

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
def handle_tile_requested_event(json):
	print request.sid, type(request.sid)
	gamecontroller.request_tile(request.sid)

<<<<<<< HEAD
@socketio.on("choose tile")
def handle_tile_requested_event(something):
	print "Choose tile request", str(something), "from main.py"
	gamecontroller.choose_tile(something)


=======
>>>>>>> f9644ab1af7c508135d1a840704ebcf410eb9260

############################
################### Run
###########################

port = int(os.environ.get('ROVPORT',8080))

if __name__ == '__main__':
    socketio.run(app,'0.0.0.0',port)

