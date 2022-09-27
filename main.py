import os
from typing import NoReturn
from unittest import result
from projeto import *
from time import sleep

if __name__ == '__main__':
  acaoComprada = FilaArray()
  acaoVendida = FilaArray()
  capital = FilaArray()

  clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
  clear()

  def apresentacao() -> bool:
    print('\nO programa recebe dois tipos de entradas compras e vendas e para difereciar uma da outra precisa por a inicial de transação que é "c" para compras e "v" para vendas.\nEx: 100 30 c.')
    inicializador = input('\nPara iniciar o processo digite "start", para saber o total das ações digite "amount", para saber o valor do capital que possui digite "wallet" e para sair digite "exit": ').lower().strip()

    if inicializador == 'start':
      return True
    elif inicializador == 'amount':
      print('\nAinda não a valores para saber o total!')
      sleep(3)
      clear()
      apresentacao()
      return True
    elif inicializador == 'wallet':
      print('\nAinda não a valores para saber o total!')
      sleep(3)
      clear()
      apresentacao()
      return True
    elif inicializador == 'exit':
      return False
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!')
      sleep(3)
      clear()
      apresentacao()
      return True

  def compras(valores) -> NoReturn:
    acaoComprada.enqueue(valores)

  def vendas(valores) -> NoReturn:
    acaoVendida.enqueue(valores)

  def total(acoes: FilaArray, name: str):
    print(f'<----{name}---->')
    valorAcao = 0
    for index in range(acoes._tamanho):
      firstAcao = acoes.dequeue()
      unidade = 1
      for i in firstAcao:
        unidade *= float(i)
      
      valorAcao += unidade
    print(f'valor {name} R$: {valorAcao:.2f}')

  def wallet():
    purchaseValue: float = 0
    saleValue: float = 0
    capital: float = 0
    for index in range(acaoComprada._tamanho):
      firstPurchase = acaoComprada.dequeue()
      unidade = 1
      for i in firstPurchase:
        unidade *= float(i)
      purchaseValue += unidade

      for index in range(acaoVendida._tamanho):
        firstSale = acaoVendida.dequeue()
        unidade = 1
        for i in firstSale:
          unidade *= float(i)
        saleValue += unidade
      print('compra =>', purchaseValue)
      print('venda =>', saleValue)
      
      capital += saleValue - purchaseValue
    print(capital)

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
        transacoes = input('Informe a quantidade, valor e o tipo de transição: ').lower().strip()
        if transacoes == 'exit':
          break
        elif transacoes == 'amount':
          total(acaoComprada, 'compras')
          total(acaoVendida, 'vendas')
          break
        elif transacoes == 'wallet':
          wallet()
          break

        transacoes = transacoes.split()
        if transacoes[2] == 'c':
          compras(transacoes[:2])
        elif transacoes[2] == 'v':
          vendas(transacoes[:2])

        dia+=1

dias()