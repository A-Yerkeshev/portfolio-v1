import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4321))
    app.run(host='0.0.0.0', port=port)
    app.debug = True
