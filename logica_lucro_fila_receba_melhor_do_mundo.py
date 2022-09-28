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
      #raise FilaVazia('A Fila está vazia')
      return False
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
    result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
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

acoes_compradas.enqueue('100 20')
acoes_compradas.enqueue('20 24')
acoes_compradas.enqueue('200 36')

acoes_vendidas.enqueue('320 30')

total_compradas = 0
total_vendidas = 0

if __name__ == '__main__':
    while True:
        try:
            q_c, v_c = acoes_compradas.dequeue().split(' ') 
            quant_compradas.enqueue(q_c)
            valor_compradas.enqueue(v_c)

            try:
                q_v, v_v = acoes_vendidas.dequeue().split(' ')
                quant_vendidas.enqueue(q_v)
                valor_vendidas.enqueue(v_v)
            except:
                pass
            
        except:
            break
        
        
        
    quant_compradas.show()
    valor_compradas.show()

    quant_vendidas.show()
    valor_vendidas.show()
    
    # [100, 20, 200, ]

    # [150, ] 
    while True:
        i = int(quant_vendidas.dequeue())
        j = int(quant_compradas.dequeue())
        
        sub = i - j
        if sub > 0:
            quantidades.enqueue(j)
            quantidades_copia.enqueue(j)
            quant_vendidas.enqueue(sub)
            i = sub
        elif sub <= 0:
            quantidades.enqueue(i)
            quantidades_copia.enqueue(i)
            if sub > 0:
              resto.enqueue(abs(sub))
            break
          
        
                
    quantidades.show()
    quantidades_copia.show()
    
    while True:
        if quantidades.is_empty():
            break
        else:
            mult = int(quantidades.dequeue()) * int(valor_compradas.dequeue())
            real_compradas.enqueue(mult)
            
    real_compradas.show()
    
    while True:
        if quantidades_copia.is_empty():
            break
        else:
            x = int(valor_vendidas.dequeue())
            multi = int(quantidades_copia.dequeue()) * x
            valor_vendidas.enqueue(x)
            real_vendidas.enqueue(multi)
            
    real_vendidas.show()
    
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
       
            
    print(total_compradas)
    print(total_vendidas)
    print(f'Lucro: {total_vendidas - total_compradas}')
    print(resto)

        
    
    
    
    

    

    
    
            
        
