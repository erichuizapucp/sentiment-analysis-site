import flask as f

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('page/one-column.html', title='Introducción')


@app.route('/state-of-art')
def sate_of_art():
    return render_template('page/one-column.html', title='Estado del Arte')


@app.route('/dataset')
def dataset():
    return render_template('page/one-column.html', title='Conjunto de Datos')


@app.route('/method')
def method():
    return render_template('page/one-column.html', title='Método')


@app.route('/results')
def results():
    return render_template('page/one-column.html', title='Resultados')


@app.route('/references')
def references():
    return render_template('page/one-column.html', title='Referencias')


if __name__ == '__main__':
    app.run()
