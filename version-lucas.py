#from msilib import PID_TITLE
from os import system, name, _exit
from tkinter import SCROLL
from typing import NoReturn
from time import sleep
from collections import deque


class FilaArray:
  def __init__(self):
    self._dados = deque([])

  def is_empty(self):
    return len(self._dados) == 0

  def dequeue(self):
    if (not self.is_empty()):
      return self._dados.popleft()
    raise Exception('Fila vazia.')

  def enqueue(self, e):
    self._dados.append(e)

  def first(self):
    return self._dados[0]

  def size(self):
    return len(self._dados)
  
  def removeLast(self):
    if (not self.is_empty()):
      return self._dados.pop()
    raise Exception ('Fila vazia')


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
  estoqueCompras.append(int(valores[0]))
  valoresCopia = valores.copy()
  valoresCopia.append('c')
  acoesCompraVenda.enqueue(valoresCopia)

def vendas(valores) -> NoReturn:
  acaoVendida.enqueue(valores)
  estoqueVendas.append(int(valores[0]))
  valoresCopia = valores.copy()
  valoresCopia.append('v')
  acoesCompraVenda.enqueue(valoresCopia)

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
  qtdAcoesCompradas = 0
  cont = 1
  tamanhoCompra = acCompra.size()
  while cont <= tamanhoCompra:
    elementoRemovido = acCompra.dequeue()
    qtdAcoesCompradas += float(elementoRemovido[0])
    
    acCompra.enqueue(elementoRemovido)
    
    cont+=1


  cont = 1
  qtdAcoesVendidas = 0
  tamanhoVenda = acVenda.size()
  while cont <= tamanhoVenda:
    elementoRemovido = acVenda.dequeue()
    qtdAcoesVendidas += float(elementoRemovido[0])
    
    acVenda.enqueue(elementoRemovido)
    
    cont+=1
    

  if qtdAcoesCompradas >= qtdAcoesVendidas:
    lucro = 0
    cont = 1
    while cont <= tamanhoVenda:
      if int(acVenda.first()[0]) > int(acCompra.first()[0]):
        acoesVendidas, precoVenda = acVenda.dequeue()
        acoesVendidas = int(acoesVendidas)
        precoVenda = float(precoVenda)

        while acoesVendidas > 0 and acCompra.size() > 0:
          if int(acCompra.first()[0]) > acoesVendidas:
            acoesCompradas, precoCompra = acCompra.dequeue()
            acoesCompradas = int(acoesCompradas)
            precoCompra = float(precoCompra)
            
            lucro += (acoesVendidas * precoVenda) - (acoesVendidas * precoCompra)
            acoesVendidas = 0
          else:
            acoesCompradas, precoCompra = acCompra.dequeue()
            acoesCompradas = int(acoesCompradas)
            precoCompra = float(precoCompra)
            
            acoesVendidas -= acoesCompradas
            lucro += (acoesCompradas * precoVenda) - (acoesCompradas * precoCompra)
          print(lucro)
        
      else:
        acoesCompradas, precoCompra = acCompra.dequeue()
        acoesCompradas = int(acoesCompradas)
        precoCompra = float(precoCompra)
        while acoesCompradas > 0 and acVenda.size() > 0:
          acoesVendidas, precoVenda = acVenda.dequeue()
          acoesVendidas = int(acoesVendidas)
          precoVenda = float(precoVenda)
          
          acoesCompradas -= acoesVendidas
          lucro += (acoesVendidas * precoVenda) - (acoesVendidas * precoCompra)

      cont += 1

    print('Seu lucro foi de ' + 'R$ ' + str(lucro))

    _exit(0)
  else:
    print('\n\nVocê vendeu mais ações do que comprou. Preencha as informações corretamente.')
    _exit(0)

def vendaMenorOuIgualACompra(acoesVendidasNow) -> bool:
    qtdAcoesCompra = 0
    for acoesCompra in estoqueCompras:
      qtdAcoesCompra += acoesCompra
  
    qtdAcoesVendas = 0
    for acoesVendas in estoqueVendas:
      qtdAcoesVendas += acoesVendas
  
    return (qtdAcoesVendas + int(acoesVendidasNow)) <= qtdAcoesCompra
    

def entradaDado(dia, contBackOperation = 1):
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
        contBackOperation = 0
        entradaDado(dia)
      elif transacoes == 'wallet':
        wallet(acaoComprada, acaoVendida)
        sleep(2)
        contBackOperation = 1
        dia = 0
        entradaDado(dia)
      elif transacoes == '<':
        if (acoesCompraVenda.size() > 0 and contBackOperation <= 10):
          ultimaOperacao = acoesCompraVenda.removeLast()
          vendaOuCompra = ultimaOperacao[2]
  
          if (vendaOuCompra == 'c'):
            acaoComprada.removeLast()
          elif vendaOuCompra == 'v':
            acaoVendida.removeLast()
  
          entradaDado(dia, contBackOperation + 1)
        else:
          print('\n\nVOCÊ NÃO PODE VOLTAR MAIS.\n\n')
          entradaDado(dia, contBackOperation + 1)

      
      contBackOperation = 1
      transacoes = transacoes.split()
      if len(transacoes) > 1:
        if transacoes[2] == 'c':
          dia+=1
          compras(transacoes[:2])
        elif transacoes[2] == 'v' and vendaMenorOuIgualACompra(transacoes[0]):
          dia+=1
          vendas(transacoes[:2])
        else: 
          print('\nQuantidade de vendas maior que a quantidades de compras')
          sleep(3)
      else:
        print('\nComando não reconhecido, digite uns dos comando expecificados!')
        sleep(3)
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

acaoComprada = FilaArray()
acoesCompraVenda = FilaArray()
acaoVendida = FilaArray()
estoqueCompras = []
estoqueVendas = []

clear = lambda: system('cls' if name == 'nt' else 'clear')
clear()

main()
