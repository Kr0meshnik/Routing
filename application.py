from flask import Flask
from flask import render_template

app = Flask('__main__')

@app.route('/map')
def index():
    return render_template('map.html')

if __name__ == '__main__':
    app.run()
