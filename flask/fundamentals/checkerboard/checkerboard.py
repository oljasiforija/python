from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('index.html')

@app.route('/4')
def eight_by_four():
    return render_template('index1.html')

@app.route('/<int:x>/<int:y>')
def by_y_and_x(x, y):
    return render_template('index2.html', x = x, y = y)

@app.route('/<int:x>/<color1>')
def by_x(x, color1):
    return render_template('index3.html', x = x, color1 = color1)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def by_all(x, y, color1, color2):
    return render_template('index4.html', x = x, y = y, color1 = color1, color2 = color2)






if __name__ == '__main__':
    app.run(debug = True)