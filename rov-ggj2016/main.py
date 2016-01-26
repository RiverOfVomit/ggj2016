from flask import Flask, render_template
app = Flask(__name__)

print("starting up server")

@app.route("/")
def hello():
    #return "Hello World!"
    return render_template('index.html')

if __name__ == "__main__":
    app.run('',8080,debug=True)