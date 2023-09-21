#Matriz usando biblioteca numpy
import numpy as np
numeros = np.array([[4,13,16],[5,7,1],[8,10,15]])
print(numeros)
minimo = numeros.min()#Função que retornar o valor minimo dentro da matriz
maximo = numeros.max()#Retorna o valor maximo dentro de uma matriz
soma = numeros.sum()#Retorna a soma de todos elementos de uma matriz
media = numeros.mean()#Retorna a media
desvio = numeros.std()#Desvio padrão
print("Minimo =", minimo)
print("Maximo =", maximo)
print('Soma =', soma)
print('Media =', media)
print('Desvio =', desvio)
 