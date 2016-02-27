from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/b")
def bu():
    return "Bubla"

if __name__ == "__main__":
    app.run()