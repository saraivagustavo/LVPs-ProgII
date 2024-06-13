#questão 1: busca sequencial
def f_pertence(l,x):
    for item in l:
        if(x == l[item]): return True
    return False

#questão 3: busca binária (retornar a posição)
def f_pertenceBinariaPos(l,x):
    esquerda = 0
    direita = len(l) - 1
    while(esquerda <= direita):
        meio = (esquerda + direita) // 2
        if(l[meio] == x): 
            return meio
        elif(l[meio] < x):
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
