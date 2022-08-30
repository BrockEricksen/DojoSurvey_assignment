from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "gjklhsgalh"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user_data', methods = ['POST'])
def user_data():
    if len(request.form['user_name']) == 0:
        return redirect('/')
    session['user_name'] = request.form['user_name']
    session['user_loc'] = request.form['user_loc']
    session['user_fav_lang'] = request.form['user_fav_lang']
    session['user_comment'] = request.form['user_comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/go_back')
def go_back():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
