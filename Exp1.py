from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/about")
def about():
    return "This is about page"


app.run(debug=True)
