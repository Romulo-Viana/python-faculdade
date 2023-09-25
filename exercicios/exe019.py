def busca(self, k):
    nóAtual=self.cabeça
    if nóAtual.chave==k:
        return nóAtual
    while nóAtual.proximo != None:
        nóAtual=nóAtual.proximo
    #passe para o próximo nó
        if nóAtual.chave==k:
            return nóAtual
        #chave encontrada
        return None
        #chave não encontrada