from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/state-of-art')
def sate_of_art():
    return render_template('state-of-art.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')


@app.route('/method')
def method():
    return render_template('method.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/references')
def references():
    return render_template('references.html')


if __name__ == '__main__':
    app.run()
