
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)

print("starting up server")

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)

@app.route("/")
def index():
    #return "Hello World!"
    return render_template('index.html')


@app.route("/client")
def client():
    #return "Hello World!"
    return render_template('client.html')


@app.route("/board")
def board():
	#return "Board is up!"
	return renter_template("board.html")


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on("echo")
def handle_my_custom_event(string):
	emit("This is echo alpha seven", string)
	print "Echo sent"
	# All clients will messages from emit().


if __name__ == "__main__":
    #app.run('',8080,debug=True)
    socketio.run(app,'0.0.0.0',8080)
