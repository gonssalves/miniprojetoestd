#from msilib import PID_TITLE
from os import remove, system, name, _exit
from tkinter import SCROLL
from typing import NoReturn
from time import sleep

from classe import *
from lucro import *


if __name__ == '__main__':
    
    clear = lambda: system('cls' if name == 'nt' else 'clear')
    clear()
    
    def apresentacao() -> bool:
        print('\nO programa recebe dois tipos de entradas compras e vendas e para difereciar uma da outra precisa por a inicial de transação que é "c" para compras e "v" para vendas.\nEx: 100 30 c.')
        inicializador = input('\nPara iniciar o processo digite "start", para ver o lucro digite "wallet", para descarta a última operação digite "<" e para sair digite "exit": ').lower().strip()

        if inicializador == 'start':
            return True
        elif inicializador == 'wallet':
            print('\nAinda não há valores para saber o total!')
            sleep(3)
            clear()
            apresentacao()
            return True
        elif inicializador == '<':
            print('\nAinda não há operações para serem desfeitas')
            sleep(3)
            clear()
            apresentacao()
        elif inicializador == 'exit':
            return False
        else:
            print('\nComando não reconhecido, digite uns dos comando expecificados!')
            sleep(3)
            clear()
            apresentacao()
            return True
        
    def compras(valores) -> NoReturn:
        acoes_compradas.enqueue(valores)

    def vendas(valores) -> NoReturn:
        acoes_vendidas.enqueue(valores)
        
        
    def entradaDado(dia):
        count_desfaz = 0
        count = ''
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
                elif transacoes == 'wallet':
                    valida_quantidades()
                    return False
                elif transacoes == '<':
                    if count == 'c':
                        if count_desfaz == 10:
                            print('Você chegou ao limite de operações desfeitas')
                            sleep(2)
                        elif acoes_compradas.remove_last():
                            count_desfaz += 1
                            print('< c', count_desfaz)
                            sleep(2)
                        else:
                            print('Nenhuma operação para ser desfeita')
                            sleep(2)
                    elif count == 'v':
                        if count_desfaz == 10:
                            print('Você chegou ao limite de operações desfeitas')
                            sleep(2)
                        elif acoes_vendidas.remove_last():
                            count_desfaz += 1
                            print('< v', count_desfaz)
                            sleep(2)
                        else:
                            print('Nenhuma operação para ser desfeita')
                            sleep(2)
                    else:
                        print('Nenhuma operação para ser desfeita')
                        
                else:    
                    q, v, t = transacoes = transacoes.split()

                    if len(transacoes) > 1:
                        if t == 'c':
                            dia+=1
                            acoes_geral.enqueue(q + ' ' + v)
                            count_desfaz = 0
                            count = 'c'
                            compras(q + ' ' + v)
                        elif t == 'v':
                            if acoes_compradas.is_empty():
                                print('Nenhuma ação foi comprada')
                                sleep(3)
                            else:
                                dia+=1
                                acoes_geral.enqueue(q + ' ' + v)
                                count_desfaz = 0
                                count = 'v'
                                vendas(q + ' ' + v)
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


main()
