import numpy as np
from neupy import algorithms
from neupy import environment
from neupy import plots
import matplotlib.pyplot as plt
from padroes import *
import random

def criar_ruidos(redeHopfield, number, percentagem, num_testes):
    erro_percentagem = []
    erro_precisao = []
    erro_total = []
    numero_ruido = np.copy(number) 

    for k in range(0, int(num_testes)):
        
        num_errors = 120 * (int(percentagem))/100
        random_index_erros = []


        for i in range(0,int(num_errors)):
            numero_aleat = random.randint(1, 120)
            if numero_aleat in random_index_erros:
                random_index_erros.append(numero_aleat+random.randint(1,120))
            else:
                random_index_erros.append(numero_aleat)

        for i in range(0, 120):
            if i in random_index_erros:
                if numero_ruido.item(i) == 0:
                    np.put(numero_ruido, [i], [1])
                else:
                    np.put(numero_ruido, [i], [0])
        
        result = redeHopfield.predict(numero_ruido)  
        diferenca = diferenca_padroes(number, result)
        acerto_ou_erro = diferenca_hamming(number, result)
        erro_percentagem.append(round(diferenca,2))
        if(acerto_ou_erro == True):
            erro_precisao.append(1)
        else:
            erro_precisao.append(0)

        '''
        print("----------------------------------")
        print(desenhar_padrao(number.reshape(12,10)))
        print("----------------------------------")


        print("----------------------------------")   
        print(desenhar_padrao(numero_ruido.reshape(12,10)))
        print("----------------------------------")

        print("----------------------------------")   
        print(desenhar_padrao(result.reshape(12,10)))
        print("----------------------------------")
        '''
       
    erro_total.append(erro_percentagem)
    erro_total.append(erro_precisao)
    
    return erro_total


def desenhar_padrao(matrix_imagem):
    for row in matrix_imagem.tolist():
        print('| ' + ' '.join(' #'[val] for val in row))
    

def diferenca_padroes(numero, resultado):
    diferente = 0
    for i in range (0, 120):
        if numero.item(i)==resultado.item(i):
            continue
        else:
            diferente = diferente+1
    return diferente/120


def diferenca_hamming(numero, resultado):
    bit_igual = 0
    for i in range (0, 120):
        if numero.item(i)==resultado.item(i):
            bit_igual = bit_igual+1
        else:
            continue
    if(bit_igual == 120):
        return True
    else:
        return False
