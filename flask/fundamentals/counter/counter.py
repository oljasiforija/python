from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counterbelieveitornot'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] +=1



    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def increment_counter():
    print (request.form["button_clicker"])
    session['counter'] += 0
    return redirect('/')

@app.route('/counter1', methods=['POST'])
def increment_counter1():
    print (request.form["button_clicker1"])
    session['counter'] += 1
    return redirect('/')

@app.route('/counter2', methods=['POST'])
def increment_counter2():
    print(request.form['input_x'])
    session['counter'] += int(request.form['input_x'])
    return redirect('/')



@app.route('/destroy_session', methods= ['POST'])
def reset_counter():
    session.clear()
    return redirect('/')





if __name__ == '__main__':
    app.run(debug = True)