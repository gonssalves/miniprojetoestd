from typing import NoReturn
from time import sleep

from classe import *

def valida_quantidades(am = 0) -> bool:
    valida1 = 0
    valida2 = 0
    
    if am == 0:
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
        
        if valida1 - valida2 < 0:
            sleep(3) 
            return False
        else:
            acoes_compradas.enqueue(abs(valida2-valida1)) 
            calcula_lucro()

    
# quant_compradas.show()
# valor_compradas.show()

# quant_vendidas.show()
# valor_vendidas.show()

def total(Cquant: int, Cvalor: int, Vquant: int, Vvalor: int):
    if Cquant * Cvalor > 0 and Vquant * Vvalor > 0:
        t_c = Cquant * Cvalor
        t_v = Vquant * Vvalor
        print(f'Valor das ações compradas: {t_c}'), print(f'Valor das ações vendidas: {t_v}')
    else:
        print(f'Valor das ações compradas: {t_c}'), print(f'Valor das ações vendidas: {t_v}')
        
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
            break
        elif sub == 0:
            if quant_compradas.is_empty and quant_vendidas.is_empty():
                quantidades.enqueue(i)
                quantidades_copia.enqueue(i)
                break
            
    # quantidades.show()
    # quantidades_copia.show()
    
    while True:
        if quantidades.is_empty():
            break
        else:
            x = valor_compradas.dequeue()
            mult = quantidades.dequeue() * x
            #valor_compradas.enqueue(x)
            real_compradas.enqueue(mult)
            if len(valor_compradas) == 0:
                acoes_compradas.enqueue(x)
    # real_compradas.show()
    
    while True:
        if quantidades_copia.is_empty():
            break
        else:
            x = valor_vendidas.dequeue()
            multi = quantidades_copia.dequeue() * x
            valor_vendidas.enqueue(x)
            real_vendidas.enqueue(multi)
            
    # real_vendidas.show()

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
