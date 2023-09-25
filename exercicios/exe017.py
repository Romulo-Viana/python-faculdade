#Função com desempacotamento *, que pode receber quantidade de valores diferentes
def contador(* num):
    tam = len(num)
    print(f"O tamanho de {num} e são ao todo {tam}")


contador(4)
contador(4,5,7,1,3)
contador(8,10,5)