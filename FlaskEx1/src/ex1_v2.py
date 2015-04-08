from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return ('<html><head><title>WakeKill</title></head>' + 
    '<body><h1>Ambient Intelligence 2015</h1>' +
    '<p>Welcome to the WakeKill project.</p>' +
    '<p><img src="'+url_for('static', filename='rooster.jpg')+'"></p>' +
    '<p>&copy; <a href="' + url_for('about') + '">SmartRooster</a></p>' +
    '</body></html>' )
    
@app.route('/about.html')
def about():
    return ( '<html><head><title>WakeKill</title></head>' +
    '<body><h1>SmartRooster - About us</h1>' +
    '<p>This group if composed by the greatest sleepers in the class.</p>' +
    '<p>If  it wakes us up, you may bet it&apos;ll work for you, too.</p>' +
    '<h1>Try our <a href="'+ url_for('index')+'">WakeKill</a> project</h2>' +
    '</body></html>' )

if __name__ == '__main__':
    app.run(debug=True)