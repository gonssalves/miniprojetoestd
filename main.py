from typing import NoReturn
from projeto import *

if __name__ == '__main__':
  compradas = FilaArray()
  vendidas = FilaArray()
  capital = FilaArray()


  def apresentacao() -> bool:
    print('''
O programa recebe dois tipos de entradas compras e vendas e para difereciar uma da outra
precisa por a inicial de transação que é "c" para comopras e "v" para vendas.''')
    inicializador = input('''
Para iniciar o processo digite "start", para saber o resultado digite "result" e para parar digite "exit": ''').lower()

    if inicializador == 'start':
      return True
    elif inicializador == 'result':
      print('Ainda não a valores para saber o resultado!')
      apresentacao()
    else:
      return False

  def compras(valores) -> NoReturn:
    compradas.enqueue(valores)

  def vendas(valores) -> NoReturn:
    vendidas.enqueue(valores)

  def resultado():
    print('<----compras---->')
    compradas.show()
    print('<----vendas---->')
    vendidas.show()

  def dias() -> NoReturn :
    if apresentacao():
      dia = 1
      while True:
        print(
        f'''
        \t================
        \t||    Dia {dia}   ||
        \t================
        ''')
        transacoes = input('Informe a quantidade, valor e o tipo de transição: ').lower()
        if transacoes == 'exit':
          break
        elif transacoes == 'result':
          resultado()
          break

        transacoes = transacoes.split()
        if transacoes[2] == 'c':
          compras(transacoes[:2])
        elif transacoes[2] == 'v':
          vendas(transacoes[:2])

        dia+=1

dias()