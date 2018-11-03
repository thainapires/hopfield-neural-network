import numpy as np
from neupy import algorithms
from neupy import environment
from neupy import plots
import matplotlib.pyplot as plt
from padroes import *
from comparacao import *

#Padroes de 0 a 9 estao no arquivo chamado padroes, que é importado
numeros = np.concatenate([zero, one, two, three, four, five, six, seven, eight, nine], axis=0)

#Rede Hopfield é criada e treinada com os numeros
redeHopfield = algorithms.DiscreteHopfieldNetwork(mode='sync')
redeHopfield.train(numeros)

#Função que retorna um array de arrays
erro = criar_ruidos(redeHopfield, seven, 5, 5)

#A primeira posição do array representa as porcentagens de erro em relação
#a quantidade de bits diferentes entre o padrão esperado e o padrão encontrado pela rede
porcBitsErrados = np.array(erro[0])
print('Média das porcentagens de bits errados:', np.mean(porcBitsErrados))

#A segunda posição do array é um array com valores binários, onde 1 representa
#que a rede acertou o padrão esperado com precisão de 100% e 0 caso a rede tenha
#errado pelo menos um bit
porcAcerto = np.array(erro[1])
print('Média dos acertos (Predição com bits 100% iguais):', np.mean(porcAcerto))
