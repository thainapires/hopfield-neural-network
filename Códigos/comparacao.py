import numpy as np
from neupy import algorithms
from neupy import environment
from neupy import plots
import matplotlib.pyplot as plt
from padroes import *
import random

def create_half_patterns(dhnet,numberarr, percentage, num_testes):
    error_percentagem_test = []
    error_accuracy_test = []
    error_total = []
    numbererrorarr = np.copy(numberarr) 
    for k in range(0, int(num_testes)):
        num_errors = 120 * (int(percentage))/100
        random_index_erros = []
        #print (num_errors)
        for i in range(0,int(num_errors)):
            random_num = random.randint(1, 120)
            if random_num in random_index_erros:
                random_index_erros.append(random_num+random.randint(1,120))
            else:
                random_index_erros.append(random_num)
        #print (random_index_erros)
        for i in range(0, 120):
            if i in random_index_erros:
                if numbererrorarr.item(i) == 0:
                    np.put(numbererrorarr, [i], [1])
                else:
                    np.put(numbererrorarr, [i], [0])
        
        result = dhnet.predict(numbererrorarr)  
        dif = diferencapadroes(numberarr, result)
        dif2 = diferencahamming(numberarr, result)
        error_percentagem_test.append(round(dif,2))
        if(dif2 == True):
            error_accuracy_test.append(1)
        else:
            error_accuracy_test.append(0)
        '''
        print("----------------------------------")
        print(desenhar_padrao(numberarr.reshape(12,10)))
        print("----------------------------------")


        print("----------------------------------")   
        print(desenhar_padrao(numbererrorarr.reshape(12,10)))
        print("----------------------------------")

        print("----------------------------------")   
        print(desenhar_padrao(result.reshape(12,10)))
        print("----------------------------------")
        '''
       
    error_total.append(error_percentagem_test)
    error_total.append(error_accuracy_test)
    return error_total


def desenhar_padrao(image_matrix):
    for row in image_matrix.tolist():
        print('| ' + ' '.join(' #'[val] for val in row))
    

def diferencapadroes(numero, resultado):
    diferente = 0
    for i in range (0, 120):
        if numero.item(i)==resultado.item(i):
            continue
        else:
            diferente = diferente+1

    return diferente/120


def diferencahamming(numero, resultado):
    igual = 0
    for i in range (0, 120):
        if numero.item(i)==resultado.item(i):
            igual = igual+1
        else:
            continue
    if(igual == 120):
        return True
    else:
        return False
