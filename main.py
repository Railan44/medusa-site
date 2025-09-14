from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

links = [
    {"url": "/inicio", "img": "/static/img/inicio.PNG", "text": "Inicio"},
    {"url": "/explorer", "img": "/static/img/explorer.png", "text": "Explore"},
    {"url": "/shorts", "img": "/static/img/shorts.png", "text": "Shorts"},
    {"url": "/inscritos", "img": "/static/img/inscritos.png", "text": "Inscritos"},
    {"type": "divider"},
    {"url": "/biblioteca", "img": "/static/img/biblioteca.png", "text": "Biblioteca"},
    {"url": "/historico", "img": "/static/img/sininho.png", "text": "Notificações"},
    {"url": "/seus-videos", "img": "/static/img/seus-videos.png", "text": "Seus Videos"},
    {"url": "/veja-depois", "img": "/static/img/veja-depois.png", "text": "Veja depois"},
]


@app.route('/', methods= ['GET', 'POST'])
def index():
    return render_template('index.html', links=links)


@app.route('/inscritos')
def inscritos():
    return render_template('inscritos.html')

@app.route('/Registro')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)