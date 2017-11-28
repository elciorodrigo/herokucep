from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask(__name__)



@app.route("/")
def hello_word():
    return render_template('cep.html')

@app.route('/consultar')
def consultarCep():
    data = efetuar_consulta(request.args.get('cep'))
    return render_template('hello.html', data=data)

def efetuar_consulta(cep):
    req = 'https://viacep.com.br/ws/' + cep + '/json/'
    response = requests.get(req)

    if (response.status_code != 200):
        data = {'erro': "consulta nao retornou resultados"}
    else:
        data = {'bairro': response.json().get("bairro"),
                'logradouro': response.json().get("logradouro"),
                'localidade': response.json().get("localidade"),
                'cep': response.json().get("cep")}
    return data;



app.run()