from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'THEresults'


@app.route('/')
def route():
    return render_template('index.html')
@app.route('/survey', methods = ['POST'])
def survey():
    print(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')
    

if __name__ == '__main__':
    app.run(debug = True)