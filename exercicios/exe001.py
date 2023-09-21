#Matriz em linguagem Python

compras = [["arroz",6],["feijão",5,1],["carne",50,2]]
print(compras)
compras.append(["cebola",5,1])
print(compras)
compras[0].append(2)
print(compras)
compras.remove(["feijão",5,1])
print(compras)
compras.pop(2)
print(compras)