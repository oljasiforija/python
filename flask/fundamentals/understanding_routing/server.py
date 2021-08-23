from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'hello world'

@app.route('/Dojo')

def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:x>/<string:y>')
def repeat(x, y):
    return x * y


if __name__ == '__main__':
    app.run(debug = True)