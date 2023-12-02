produtos = [
  { 'nome': 'feijão', 'preco': 5.00, 'estoque': 250 },
  { 'nome': 'arroz', 'preco': 4.00, 'estoque': 120 },
  { 'nome': 'açúcar', 'preco': 3.00, 'estoque': 340 },
  { 'nome': 'macarrão', 'preco': 1.50, 'estoque': False },
  { 'nome': 'sal', 'preco': 1.00, 'estoque': 70 },
  { 'nome': 'bolacha', 'preco': 1.50, 'estoque': 0 },
]

def get_produto(nome):
  for produto in produtos:
    if produto['nome'] == nome:
      return produto
  return None
