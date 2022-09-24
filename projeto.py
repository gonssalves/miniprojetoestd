class FilaVazia(Exception):
    ...

class FilaArray:
  
  def __init__(self):
    self._dados = []
    self._tamanho = 0
    self._inicio = 0

  def __len__(self): 
    return self._tamanho

  def is_empty(self):
    return self._tamanho == 0

  def enqueue(self, e):  
    self._dados += e
    
  def dequeue(self):
    result = self._dados.pop(0)
    return result                         

  def show(self):
    print(self._dados)
