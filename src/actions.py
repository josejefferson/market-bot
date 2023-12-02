import database
from struct import Struct

def consulta_preco(parameters: Struct):
  nome = parameters['produto']
  if not nome:
    return 'Por favor, informe o nome do produto'

  produto = database.get_produto(nome)
  if produto:
    return f'O preço do {produto["nome"]} é {produto["preco"]}'
  else:
    return f'O produto com o nome "{nome}" não foi encontrado'


def consulta_estoque(parameters: Struct):
  nome = parameters['produto']
  if not nome:
    return 'Por favor, informe o nome do produto'

  produto = database.get_produto(nome)
  if produto:
    estoque = produto["estoque"]
    if estoque > 1:
      return f'Temos {estoque} unidades de {produto["nome"]} no estoque'
    elif estoque == 1:
      return f'Temos apenas 1 unidade de {produto["nome"]} no estoque, corre para adquiri-la!'
    elif estoque == 0:
      return f'Infelizmente não temos {produto["nome"]} no estoque'
    else:
      return f'Desculpe, não sei informar se tempos {produto["nome"]} no estoque. Por favor, pergunte a algum atendente do supermercado'
  else:
    return f'O produto com o nome "{nome}" não foi encontrado'

acoes = {
  'consulta_preco': consulta_preco,
  'consulta_estoque': consulta_estoque
}

def run(acao, parameters):
  if acao in acoes:
    action = acoes[acao]
    return action(parameters)
