from flask import Flask, render_template, Request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/index")
def hello():
    return "Hello World!"

if __name__ == "__main__":
 app.run()