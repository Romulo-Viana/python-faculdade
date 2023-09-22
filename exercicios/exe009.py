import numpy as np
vendedores=np.array(["Marcos","Ana","Juli","Piter"])
vendas=np.array([15,20,10,30])


#Para cada venda e vendedor em vendedores ENUMERE 
for indice, vendedor in enumerate(vendedores): 
    print(vendedor)
    print(vendas[indice])
    
    
#Se você precisar relacionar item de mesmo indice em listas diferentes usa-se ZIP. As listas devem ter o mesmo tamanho
for vendedor, venda in zip(vendedores, vendas):
    print(vendedor,venda)
    