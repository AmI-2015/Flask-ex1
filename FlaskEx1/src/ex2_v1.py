from flask import Flask
from flask import render_template, request, session, url_for
from werkzeug import redirect

app = Flask(__name__)
app.secret_key = 'whoknowsthissecretw'

@app.route('/')
def index():
    return render_template('index2.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    session['user'] = user
    return render_template('welcome.html', user=user)

@app.route('/logout')
def logout():
    del session['user']
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)