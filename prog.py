import os
from peewee import *
import datetime

arq = 'C:/Users/Franke/Desktop/prog/trab.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class GrupoEscoteiro(BaseModel):
    numeral = IntegerField()
    nome = CharField()
    num_tropas = IntegerField()

class Escotista(BaseModel):
    nome = CharField()
    idade = IntegerField()
    dat_ingresso = DateField()

class Ramo(BaseModel):
    nome = CharField()
    qnt_patrulha = IntegerField()

class Escoteiro(BaseModel):
    nome = CharField()
    idade = IntegerField()
    dat_ingresso = DateField()
    ramo = ForeignKeyField(Ramo)
    monitor = BooleanField()
    sub_monitor = BooleanField()

class Patrulha(BaseModel):
    nome = CharField()
    qnt_integrantes = IntegerField()
    monitor = ForeignKeyField(Escoteiro, related_name='monitor_id')
    sub_monitor = ForeignKeyField(Escoteiro)

class CaixaDaPatrulha(BaseModel):
    qnt_itens = IntegerField()
    cor_caixa = CharField()
    nome_patrulha = ForeignKeyField(Patrulha)

class GritoDaPatrulha(BaseModel):
    txt_grito = CharField()
    dat_criacao = DateField(CharField)
    nom_patrulha = ForeignKeyField(Patrulha)

class Evento(BaseModel):
    nome = CharField()
    dat_evento = DateField()
    qnt_participantes = IntegerField()

class Premiacao(BaseModel):
    nome = CharField()
    dat = DateField()

class Espera(BaseModel):
    nome = CharField()
    idade = IntegerField()


if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([GrupoEscoteiro, Escotista, Ramo, Escoteiro, Patrulha, CaixaDaPatrulha, GritoDaPatrulha, Evento, Premiacao, Espera])


    ge_dc = GrupoEscoteiro.create(numeral= 17, nome= "Duque de Caxias", num_tropas= 6)

    ch_fabio = Escotista.create(nome= 'Fábio Naguel', idade= 45, dat_ingresso = datetime.date(2014, 6, 12))

    ramo_senior = Ramo.create(nome= 'Sênior', qnt_patrulha= 5)

    es_franke = Escoteiro.create(nome= 'Vinicius Franke da Silva', idade= 17, dat_ingresso= datetime.date(2008, 6, 12), ramo= ramo_senior, monitor= False, sub_monitor= False)
    es_luizi = Escoteiro.create(nome= 'Luizi Pires', idade= 18, dat_ingresso= datetime.date(2015, 6, 12), ramo= ramo_senior, monitor= True, sub_monitor= False)
    es_thais = Escoteiro.create(nome= 'Thais Guerra', idade= 17, dat_ingresso= datetime.date(2011, 6, 12), ramo= ramo_senior, monitor= False, sub_monitor= True)

    pa_k2 = Patrulha.create(nome= 'K2', qnt_integrantes= 6, monitor= es_luizi, sub_monitor= es_thais)

    cx_k2 = CaixaDaPatrulha.create(qnt_itens = 27, cor_caixa= 'vermelha', nome_patrulha= pa_k2)

    gt_k2 = GritoDaPatrulha.create(txt_grito= 'Das montanhas mais altas, k2 é a segunda, de pedra nós somo o topo do mundo, k2 k2 k2', dat_criacao= 2003, nom_patrulha= pa_k2 )

    arsc_2017 = Evento.create(nome= 'Acampamento Regional de Santa Catarina - 2017', dat_evento= datetime.date(2017, 6, 12), qnt_participantes= 2000)

    pre_gra_azul = Premiacao.create(nome= 'Prêmio Gralha Azul - 2017', dat= datetime.date(2017, 6, 17))

    esp_pedro = Espera.create(nome= 'Pedro da Silva', idade= 13)


    