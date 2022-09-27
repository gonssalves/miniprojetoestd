from os import system, name, _exit
from typing import NoReturn
from projeto import *
from time import sleep

if __name__ == '__main__':
  acaoComprada = FilaArray()
  acaoVendida = FilaArray()
  capital = FilaArray()

  clear = lambda: system('cls' if name == 'nt' else 'clear')
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
    copyacoes = acoes._dados.copy()
    print(f'\n<----{name}---->')
    valorAcao = 0
    for index in range(len(copyacoes)):
      firstAcao = copyacoes[index]
      if firstAcao != None:
        unidade = 1
        for i in firstAcao:
          unidade *= float(i)

        valorAcao += unidade
    print(f'valor {name} R$: {valorAcao:.2f}')

  def wallet(acCompra: FilaArray, acVenda: FilaArray):
    copyCompras = acCompra._dados.copy()
    copyVendida = acVenda._dados.copy()
    purchaseValue: float = 0
    saleValue: float = 0
    capital: float = 0

    for index in range(len(copyCompras)):
      firstPurchase = copyCompras[index]
      unidade = 1
      if firstPurchase != None:
        for i in firstPurchase:
          unidade *= float(i)
        purchaseValue += unidade

    if len(copyVendida) > 0:
        for index in range(len(copyVendida)):
          firstSale = copyVendida[index]
          unidade = 1
          if firstSale != None:
            for i in firstSale:
              unidade *= float(i)
            saleValue += unidade

        capital += saleValue - purchaseValue
        print(capital)
    else:
      print(f'\nVocê não possui vendas seu valor em compras é R$: {purchaseValue:.2f}')

  def entradaDado(dia):
    try:
      while True:
        print(
        f'''
        \t================
        \t||    Dia {dia}   ||
        \t================
        ''')
        transacoes = input('Informe a quantidade, valor e o tipo de transição: ').lower().strip()
        if transacoes == 'exit':
          _exit(0)
        elif transacoes == 'amount':
          total(acaoComprada, 'compras')
          total(acaoVendida, 'vendas')
          sleep(2)
          entradaDado(dia)
        elif transacoes == 'wallet':
          wallet(acaoComprada, acaoVendida)
          sleep(2)
          entradaDado(dia)

        transacoes = transacoes.split()
        if len(transacoes) > 1:
          if transacoes[2] == 'c':
            dia+=1
            compras(transacoes[:2])
          elif transacoes[2] == 'v':
            dia+=1
            vendas(transacoes[:2])
    except Exception as e:
      if e:
        print(e)
      print('\nComando não reconhecido, digite uns dos comando expecificados!')
      sleep(3)
      clear()
      entradaDado(dia)


  def main() -> NoReturn :
    try:
      if apresentacao():
        entradaDado(1)
    except Exception as e:
      print(e)


main()