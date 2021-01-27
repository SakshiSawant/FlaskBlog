'''from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')



@app.route("/about")
def about():
    name = "Krishna"
    return render_template('about.html', name2 = name)'''

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

app.run(debug=True)
