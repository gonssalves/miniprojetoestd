from typing import NoReturn

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
      # return False
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, e):  # - - x x x -
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
      self._dados[k] = dados_antigos[posicao]  # intentionally shift indices
      # use dados_antigos size as modulus
      posicao = (1 + posicao) % len(dados_antigos)
    self._inicio = 0                          # front has been realigned

  def removeLast(self):
    ultimaPosicaoOcupada = ((self._inicio + self._tamanho) %
                            len(self._dados)) - 1

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
    result += f'] tamanho: {len(self)} capacidade {len(self._dados)}'
    return result


acoes_compradas = Fila(10)
acoes_vendidas = Fila(10)

quant_compradas = Fila(10)
quant_vendidas = Fila(10)


valor_compradas = Fila(10)
valor_vendidas = Fila(10)

quantidades = Fila(10)
quantidades_copia = Fila(10)

real_compradas = Fila(10)
real_vendidas = Fila(10)

resto = Fila(10)

def valida_quantidades() -> bool:
    valida1 = 0
    valida2 = 0
    while True:
        if acoes_compradas.is_empty():
            break
        else:
            q_c, v_c = acoes_compradas.dequeue().split(' ')
            q_c, v_c = int(q_c), int(v_c)
            quant_compradas.enqueue(q_c)
            valor_compradas.enqueue(v_c)
            valida1 += q_c

    while True:
        if acoes_vendidas.is_empty():
            break
        else:
            q_v, v_v = acoes_vendidas.dequeue().split(' ')
            q_v, v_v = int(q_v), int(v_v)
            quant_vendidas.enqueue(q_v)
            valor_vendidas.enqueue(v_v)
            valida2 += q_v

    if valida2 - valida1 > 0: raise FilaVazia('Quantidade de ações vendidas ultrapassou a quantidade de ações compradas')
    else: calcula_lucro()
        
def calcula_lucro() -> NoReturn:
    valida_quant_vendidas = 0
    total_compradas = 0
    total_vendidas = 0

    while True:
        if quant_vendidas.is_empty():
            break
        else:
            b = quant_vendidas.dequeue()
            valida_quant_vendidas += b

    quant_vendidas.enqueue(valida_quant_vendidas)

    while True:
        i = quant_vendidas.dequeue()
        j = quant_compradas.dequeue()

        sub = i - j
        if sub > 0:
            quantidades.enqueue(j)
            quantidades_copia.enqueue(j)
            quant_vendidas.enqueue(sub)
            quant_compradas.enqueue(sub)
            i = sub
        elif sub < 0:
            quantidades.enqueue(i)
            quantidades_copia.enqueue(i)
            quant_compradas.enqueue(i)
            i = abs(sub)
            resto.enqueue(abs(sub))
            break
        elif sub == 0:
            if quant_compradas.is_empty and quant_vendidas.is_empty():
                quantidades.enqueue(i)
                quantidades_copia.enqueue(i)
                break

    while True:
        if quantidades.is_empty():
            break
        else:
            x = valor_compradas.dequeue()
            mult = quantidades.dequeue() * x
            valor_compradas.enqueue(x)
            real_compradas.enqueue(mult)

    while True:
        if quantidades_copia.is_empty():
            break
        else:
            x = valor_vendidas.dequeue()
            multi = quantidades_copia.dequeue() * x
            valor_vendidas.enqueue(x)
            real_vendidas.enqueue(multi)

    while True:
        if real_compradas.is_empty():
            break
        else:
            a = real_compradas.dequeue()
            total_compradas += a

    while True:
        if real_vendidas.is_empty():
            break
        else:
            a = real_vendidas.dequeue()
            total_vendidas += a

    print(f'Lucro: R$ {total_vendidas - total_compradas}')

    
if __name__ == '__main__':
    print("digite suas compras:")
    contBack = 0
    while True:
        entradaCompras = input()
        if entradaCompras == "x":
            break
        elif entradaCompras == '<':
            if contBack < 10:
                acoes_compradas.removeLast()
                contBack += 1
            else:
                print('Você não pode mais voltar. Você já voltou 10 operações.')
        else:
            acoes_compradas.enqueue(entradaCompras)

    print('Digite sua vendas:')
    contBack = 0
    while True:
        entradaVendas = input()
        if entradaVendas == "x":
            break
        elif entradaVendas == '<':
            if contBack < 10:
                acoes_vendidas.removeLast()
                contBack += 1
            else:
                print('Você não pode mais voltar. Você já voltou 10 operações.')
        else:
            acoes_vendidas.enqueue(entradaVendas)

    valida_quantidades()


