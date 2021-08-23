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
    session['counter'] += 1

    return redirect('/')

@app.route('/destroy_session', methods= ['POST'])
def reset_counter():
    session.clear()
    return redirect('/')





if __name__ == '__main__':
    app.run(debug = True)