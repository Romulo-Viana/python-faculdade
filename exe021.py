def BuscaBST(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    else:
        if raiz.chave < chave:
            return BuscaBST(raiz.direita, chave)
        elif raiz.chave > chave:
            return BuscaBST(raiz.esquerda, chave)
        else:
            raiz