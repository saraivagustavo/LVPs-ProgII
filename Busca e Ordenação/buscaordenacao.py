'''QUESTÃO 1: A forma mais fácil de procurar por um elemento é percorrer toda a sequência, comparando o elemento com cada um de seus itens. Este algoritmo é conhecido como busca sequencial (ou busca linear, pois sua complexidade é O(n)). Crie uma função que receba uma lista l contendo números e um número x, e retorne verdadeiro caso x ocorra em l e falso caso contrário.'''
def f_pertence(l,x):
    for item in l:
        if(x == l[item]): return True
    return False

'''QUESTÃO 3: Implemente a busca binária, que recebe uma lista l com números inteiros em ordem crescente e retorne a POSIÇÃO em que x se encontra em l(ou -1, caso a lista não contenha x)'''
def f_pertenceBinariaPosicao(l,x):
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


'''BUBBLE SORT: Implemente a versão do método Bubble Sort para ordenar os elementos de uma lista.'''
def f_troca(l, i, j): #função de troca auxiliar
    aux = l[i]
    l[i] = l[j]
    l[j] = aux 
def f_bubbleSort(l):
    verificar = True
    reps = 0
    while verificar:
        verificar = False
        for i in range(len(l)-1-reps):
            if(l[i] > l[i+1]):
                f_troca(l,i,i+1) 
                verificar = True
        reps += 1

'''SELECTION SORT: Implemente o método Selection Sort para ordenar os elementos de uma lista.'''
def f_selectionSort(l):
    for pos in range(len(l)-1):
        menor = pos
        for i in range(pos+1, len(l)):
            if(l[i] < l[menor]):
                menor = i
        f_troca(l,menor,pos)

'''INSERTION SORT: Implemente o método Insertion Sort para ordenar os elementos de uma lista.'''
def f_insertionSort(l):
    l2 = [l[0]]
    for pos in range(1,len(l)):
        i = 0
        while(i < len(l2)) and (l2[i] < l[pos]):
            i += 1
        l2.insert(i,l[pos])
    return l2

def f_insertionSort2(l): #insertion sort sem criar lista nova
    for k in range(len(l)):
        elem = l[k]
        pos = k + 1
        while(pos >= 0) and (l[pos > elem]):
            l[pos+1] = l[pos]
            pos = pos - 1
        l[pos+1] = elem

'''MERGE SORT: Implemente o método Merge Sort para ordenar os elementos de uma lista.'''
def f_intercalar(l,l1,l2):
    i = 0
    j = 0
    k = 0
    while(i < len(l1)) and (j < len(l2)):
        if(l1[i] < l2[j]):
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1
    while(i < len(l1)):
        l[k] = l1[i]
        i += 1
        k += 1
    while(j < len(l2)):
        l[k] = l2[j]
        j += 1
        k += 1

def f_mergeSort(l):
    if(len(l) <= 1):
        return l
    else:
        meio = len(l) // 2
        l1 = l[:meio] #não pega o meio
        l2 = l[meio:] #pega o meio
        f_mergeSort(l1)
        f_mergeSort(l2)
        f_intercalar(l,l1,l2)
        return l
    
'''QUICK SORT: Implemente o método Quick Sort para ordenar os elementos de uma lista.'''
def f_quickSort(l):
    if(len(l) <= 1):
        return l
    else:
        menores = []
        maiores = []
        pivo = l[0]
        for i in range(1,len(l)):
            if(l[i] < pivo):
                menores.append(l[i])
            else:
                maiores.append(l[i])
        return f_quickSort(menores) + [pivo] + f_quickSort(maiores)

from random import randint   
#função main para casos de testes
def main():
    l = []
    n = int(input("Quantos números? "))
    for i in range(n):
        l.append(randint(1,1000))
    print(f'Lista não ordenada: {l}')

    print(f'Lista ordenada: {f_quickSort(l)}')
if __name__ == "__main__":
    main()