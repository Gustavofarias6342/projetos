# funcoes.py
from dados import veiculos, motoristas

# Funções CRUD para veículos
def cadastrar_veiculo(placa, modelo, ano):
    veiculos[placa] = {'modelo': modelo, 'ano': ano}

def consultar_veiculo(placa):
    return veiculos.get(placa)

def listar_veiculos():
    return veiculos

def apagar_veiculo(placa):
    if placa in veiculos:
        del veiculos[placa]
        return True
    return False

def atualizar_veiculo(placa, modelo=None, ano=None):
    if placa in veiculos:
        if modelo:
            veiculos[placa]['modelo'] = modelo
        if ano:
            veiculos[placa]['ano'] = ano
        return True
    return False

# Funções CRUD para motoristas
def cadastrar_motorista(cpf, nome):
    motoristas[cpf] = {'nome': nome, 'veiculo': None}

def consultar_motorista(cpf):
    return motoristas.get(cpf)

def listar_motoristas():
    return motoristas

def atualizar_veiculo_motorista(cpf, placa):
    if cpf in motoristas and placa in veiculos:
        motoristas[cpf]['veiculo'] = placa
        return True
    return False
