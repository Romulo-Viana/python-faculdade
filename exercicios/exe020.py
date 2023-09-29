#Lista é uma coleção ordenada e mutável. Permite membros duplicados.
lista = ['carro', True, 2, 3.5, 'carro']
lista.append('avião') #Mutável, permite add e remove elementos
print(lista)
print(lista[0])
print(type(lista))
print('_'*30)

#Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
tupla = ('carro', True, 2, 3.5)
print(tupla)
print(tupla[1])
print(type(tupla))
print('_'*30)

#O dicionário é um coleção ordenada e mutável. Nenhum membro duplicado.
dicionario = {'nome': 'carro', 'logica': True, 'numero': 2, 'outroNumero': 3.5}
print(dicionario)
print(dicionario['logica'])
print(type(dicionario))
print('_'*30)

#Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
conjunto = {'carro', True, 2, 3.5}
conjunto.add('rosa') 
print(conjunto)
print(type(conjunto))

