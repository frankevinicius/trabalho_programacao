from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
from prog import GrupoEscoteiro, Escotista, Ramo, Escoteiro, Patrulha, CaixaDaPatrulha, GritoDaPatrulha, Evento, Premiacao,Espera

app = Flask(__name__)

@app.route("/")
def inicio():
    return "inicio"

@app.route("/listar_grupos")
def listar_grupo():
    grupo = list(map(model_to_dict, GrupoEscoteiro.select()))
    return jsonify ({'lista': grupo})

@app.route("/listar_escotistas")
def listar_escotista():
    escotista = list(map(model_to_dict, Escotista.select()))
    return jsonify ({'lista': escotista})

@app.route("/listar_ramos")
def listar_ramo():
    ramo = list(map(model_to_dict, Ramo.select()))
    return jsonify ({'lista': ramo})

@app.route("/listar_escoteiros")
def listar_escoteiro():
    escoteiro = list(map(model_to_dict, Escoteiro.select()))
    return jsonify ({'lista': escoteiro})

@app.route("/listar_patrulhas")
def listar_patrulha():
    patrulha = list(map(model_to_dict, Patrulha.select()))
    return jsonify ({'lista': patrulha})

@app.route("/listar_caixas")
def listar_caixa():
    caixa = list(map(model_to_dict, CaixaDaPatrulha.select()))
    return jsonify ({'lista': caixa})

@app.route("/listar_gritos")
def listar_grito():
    grito = list(map(model_to_dict, GritoDaPatrulha.select()))
    return jsonify ({'lista': grito})

@app.route("/listar_eventos")
def listar_evento():
    evento = list(map(model_to_dict, Evento.select()))
    return jsonify ({'lista': evento})

@app.route("/listar_premios")
def listar_premio():
    premio = list(map(model_to_dict, Premiacao.select()))
    return jsonify ({'lista': premio})

@app.route("/listar_esperas")
def listar_espera():
    espera = list(map(model_to_dict, Espera.select()))
    return jsonify ({'lista': espera})




app.run(debug=True, port = 4999)