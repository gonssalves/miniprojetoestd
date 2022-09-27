class FilaVazia(Exception):
  pass

class Fila:
  def __init__(self, capacidade):
    self._dados = [None] * capacidade
    self._tamanho = 0
    self._inicio = 0

  def __len__(self):
    return self._tamanho

  def is_empty(self):
    return self._tamanho == 0

  def first(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    return self._dados[self._inicio]

  def dequeue(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, e): # - - x x x - 
    if self._tamanho == len(self._dados):
      self._altera_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._tamanho += 1

  def _altera_tamanho(self, novo_tamanho):   
    dados_antigos = self._dados               # keep track of existing list
    self._dados = [None] * novo_tamanho       # allocate list with new capacity
    posicao = self._inicio
    for k in range(self._tamanho):            # only consider existing elements
      self._dados[k] = dados_antigos[posicao] # intentionally shift indices
      posicao = (1 + posicao) % len(dados_antigos) # use dados_antigos size as modulus
    self._inicio = 0                          # front has been realigned

  def removeLast(self):
    ultimaPosicaoOcupada = ((self._inicio + self._tamanho) % len(self._dados)) - 1

    if self._dados[ultimaPosicaoOcupada] != None:
      del self._dados[ultimaPosicaoOcupada]
    else:
      raise FilaVazia('Erro ao remover, pois a fila está vazia.')
    
  def show(self):
    print(self)

  def __str__(self):
    posicao = self._inicio
    result = "["
    for k in range(self._tamanho):
      result += str(self._dados[posicao]) + ", "
      posicao = (1 + posicao) % len(self._dados)
    result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
    return result


compras = Fila(10)
comprasCopia = Fila(10)
vendas = Fila(10)

print("digite suas compras:")
contBack = 0
while True:
  entradaCompras = input()
  if entradaCompras == "x":
    break
  elif entradaCompras == '<':
    if contBack < 10:
      compras.removeLast()
      comprasCopia.removeLast()
      contBack += 1
    else:
      print('Você não pode mais voltar. Você já voltou 10 operações.')
  else:
    compras.enqueue(entradaCompras)
    comprasCopia.enqueue(entradaCompras)

print('Digite sua vendas:')
contBack = 0
while True:
  entradaVendas = input()
  if entradaVendas == "x":
    break
  elif entradaVendas == '<':
    if contBack < 10:
      vendas.removeLast()
      contBack += 1
    else:
      print('Você não pode mais voltar. Você já voltou 10 operações.')
  else:
    vendas.enqueue(entradaVendas)

# GASTO
totalGasto = 0
totalAcoesCompradas = 0
while True:
  try:
    qtdAcoesCompradas, precoCompra = compras.dequeue().split(' ')
    qtdAcoesCompradas = int(qtdAcoesCompradas)
    precoCompra = float(precoCompra)

    totalGasto += qtdAcoesCompradas * precoCompra
    totalAcoesCompradas += qtdAcoesCompradas
  except:
    break


lucro = 0
while True:
  try:
    qtdAcoesVendidas, precoVenda = vendas.dequeue().split(' ')
    qtdAcoesVendidas = int(qtdAcoesVendidas)
    precoVenda = float(precoVenda)

    qtdAcoesCompradas, precoCompra = comprasCopia.dequeue().split(' ')
    qtdAcoesCompradas = int(qtdAcoesCompradas)
    precoCompra = float(precoCompra)

    gasto = qtdAcoesVendidas * precoCompra
    vendido = qtdAcoesVendidas * precoVenda

    lucro += vendido - gasto
    
  except:
    break


print("Seu lucro foi de " + str(lucro))
