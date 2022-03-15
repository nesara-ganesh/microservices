from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form['submit_button'] == 'Home':
            return redirect("http://0.0.0.0:5050")
        elif request.form['submit_button'] == 'Register':
            #data = requests.get('http://registration-service:5053').json()
            flash('User Registered Successfully', "green")
            return redirect(url_for('index'))
        elif request.form['submit_button'] == 'Payment':
            return redirect('http://0.0.0.0:5052')
        else:
            pass
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=5051, host="0.0.0.0")
