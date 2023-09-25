def dobra(lst):
    pos = 0
    while pos < len(lst): #Enquanto a posição atual for menor que o total da lista, continue fazendo
        lst[pos] = lst[pos] *2
        pos = pos +1
        
valores=[2,5,4,8,7]
dobra(valores)
print(valores)

valor=[2,4,5,1]

for i in valor:
    dobra1=0
    dobra1 = i * 2
    print(f"Valor {i} mutiplicado por 2 = {dobra1}")


