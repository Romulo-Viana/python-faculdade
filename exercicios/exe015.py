def buscaLista(k, L, n):
        i=0  #Nosso iterador
        índiceL=-1
        while i<n:
                if L[i]==k:           #nó encontrado
                         indiceL=i    #salva o índice
                         i=n+1        #sair do laço
                i=i+1                 #segue a procura
        return indiceL
    

nomes =['Arthur', 'Joao', 'Maria', 'Ana']
i = buscaLista ('Ana', nomes, len(nomes))
print (i)