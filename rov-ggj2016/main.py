
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

############################
################### Init
############################

app = Flask(__name__)

print("starting up server")

app.config.from_pyfile('flaskapp.cfg')

socketio = SocketIO(app)

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
################### Run
############################

if __name__ == '__main__':
    socketio.run(app,'0.0.0.0',8080)
