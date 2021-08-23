from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'helooooeogwoeg'

@app.route('/play')
def play1():
    return render_template('play3.html')

@app.route('/play/<int:y>')
def play2(y):
    return render_template('play2.html', y = y)

@app.route('/play/<int:x>/<color>')
def play3(x, color):
    return render_template('play.html', x = x, color = color)






if __name__ == '__main__':
    app.run(debug = True)