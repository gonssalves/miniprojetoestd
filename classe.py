from collections import deque

class FilaVazia(Exception):
  pass


class Fila:
  def __init__(self):
    self._dados = deque([])
    
  def __len__(self):
    return len(self._dados)

  def is_empty(self):
    return len(self._dados) == 0

  def dequeue(self):
    if (not self.is_empty()):
      return self._dados.popleft()
    raise Exception('Fila vazia.')

  def enqueue(self, e):
    self._dados.append(e)

  def size(self):
    return len(self._dados)
  
  def remove_last(self):
    if (not self.is_empty()):
      return self._dados.pop()
    raise Exception ('Fila vazia')

acoes_geral = Fila()
acoes_compradas = Fila()
acoes_vendidas = Fila()

acoes_compradas_copia = Fila()
acoes_vendidas_copia = Fila()

quant_compradas = Fila()
quant_vendidas = Fila()


valor_compradas = Fila()
valor_vendidas = Fila()

quantidades = Fila()
quantidades_copia = Fila()

real_compradas = Fila()
real_vendidas = Fila()

