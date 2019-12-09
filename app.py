import json

from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    banner = {
        "title": 'Integrantes',
        "list": [
            "Eric Raphael Huiza Pereyra",
            "Percy Tippe",
            "Jorge Pomachagua",
            "Roger Chipa Sierra"
        ]
    }

    with open('data/intro.json') as file:
        intro = json.load(file)
        return render_template('page/one-column.html', title='Introducción', data=intro, banner=banner)


@app.route('/state-of-art')
def sate_of_art():
    with open('data/state-of-art.json') as file:
        state_of_art = json.load(file)
        return render_template('page/one-column.html', title='Estado del Arte', data=state_of_art)


@app.route('/dataset')
def dataset():
    with open('data/conclusions.json') as file:
        s_dataset = json.load(file)
        return render_template('page/one-column.html', title='Conjunto de Datos', data=s_dataset)


@app.route('/method')
def method():
    with open('data/method.json') as file:
        s_method = json.load(file)
        return render_template('page/one-column.html', title='Método', data=s_method)


@app.route('/conclusions')
def results():
    with open('data/conclusions.json') as file:
        s_conclusions = json.load(file)
    return render_template('page/one-column.html', title='Conclusiones', data=s_conclusions)


@app.route('/references')
def references():
    with open('data/references.json') as file:
        s_references = json.load(file)
        return render_template('page/one-column.html', title='Referencias', data=s_references)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
