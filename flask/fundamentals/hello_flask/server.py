from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hej flask! :D'

@app.route('/another_route')
def another_route():
    return 'I am another route !!!!!'

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    # return f'the result of {x} and {y} is {x * y}'
    return render_template('multiply.html', x = x, y = y, result = x * y)

@app.route('/iseven/<int:x>')
def is_even(x):

    return render_template('iseven.html', x = x)

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x, y):
    # show user table 0 * 0 up to x * y
    results = []

    if x > 20:
        x = 20
    if y > 20:
        y = 20

    for i in range(0, y+1):
        row = []
        for j in range(0, x+1):
            row.append(i * j)
        results.append(row)

    print(results)

    # return 'table made'

    return render_template('table.html', results = results, x = x, y = y)

if __name__ == '__main__':
    app.run(debug = True)