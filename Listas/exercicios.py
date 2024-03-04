'''QUESTÃO 1: Faça uma função que crie e retorne uma lista com todos os números pares de 1 a 100, porém na ordem regressiva.'''
def f_paresRegressivo():
    l = list()
    n = int(0)

    n = 1
    while n <= 100:
        if (n % 2 == 0):
            l.append(n)
        n += 1
    l.sort()
    l.reverse()
    return l

'''QUESTÃO 2: Faça um procedimento que leia 10 números digitados pelo usuário, armazene a metade de cada um deles numa lista, e depois imprima esta lista.'''
def f_metadePrint():
    l = list()
    i = int(0)
    n = int(0)

    l = []
    i = 1
    while(i <= 10):
        n = int(input())
        n = n/2
        l.append(n)
        i+=1

    print(l)

'''QUESTÃO 3: Dado um número n, faça uma função que leia n números inteiros, e retorne uma lista com esses números.'''
def f_leitura(n):
    l = list()
    k = int(0)
    i = int(0)

    i = 1

    while(i <= n):
        k = int(input())
        l.append(k)
        i+=1

    return l

'''QUESTÃO 4: Dada uma lista e um elemento, retorne o número de ocorrências do elemento na lista.'''
def f_ocorrencia(l:list,j:int)->int:
    i = int(0)
    n = int(0)

    i = 0
    n = 0

    while i < len(l):
        if j == l[i]:
            n += 1
        i += 1

    return n

'''QUESTÃO 5: Dada uma lista de números, faça uma função que encontre e retorne o maior deles.'''
def f_maior(l):
    maior = l[0]

    for x in l:
        if (x > maior):
            maior = x

    return maior

'''QUESTÃO 6: Dada uma lista de números, faça um função que encontre e retorne o índice do maior deles.'''
def f_posicaoDoMaior(l):
    maior = int(0)
    i = int(0)
    i = 0
    maior_pos = f_maior(l)

    while i < len(l):
        if maior_pos == l[i]:
            maior = i
        i += 1

    return maior
    
'''QUESTÃO 7: Dada uma lista, faça um procedimento que inverta a ordem de seus elementos.'''
def f_troca(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux 

def f_inverter(l):
    i = int(0)
    j = int(0)
    aux = int(0)

    i = 0
    j = len(l) - 1
    

    while (i < j):  
        print(i, j) #só pra saber como tá o comportamento do i e do j
        f_troca(l, i, j)
        i += 1
        j -= 1

    print(l)

'''QUESTÃO 8: Dado um número n, retorne uma lista com os n primeiros elementos da sequência de Fibonacci.'''
def f_fibonacci(n):
    #declaração de variáveis
    a = int(0)
    b = int(0)
    l = list()
    #inicialização das variáveis
    a = 0
    b = 1
    l = []
    #processamento
    for i in range(n):
        a, b = b, a + b
        l.append(a)
    return l

'''QUESTÃO 9: Defina um procedimento que receba duas listas com a mesma quantidade de números inteiros. A primeira lista contém as abscissas de um conjunto de pontos, e a segunda contém as ordenadas desses mesmos pontos. Calcule o número x de abscissas que são pares e o número y de ordenadas quesão ímpares. Se x >= y, imprima a soma de todas as abscissas. Caso contrário, imprima o produto de todas as ordenadas.'''
def f_calcularPontos(l_abs,l_ord):
    abscissas_pares = 0
    ordenadas_impares = 0

    for abscissa in l_abs:
        if(abscissa % 2 == 0):
            abscissas_pares += 1
    for ordenada in l_ord:
        if(ordenada % 2 != 0):
            ordenadas_impares += 1
    
    if(abscissas_pares >= ordenadas_impares):
        soma = 0
        for abscissa in l_abs:
            soma += abscissa
        print(f'A soma das abscissas é: {soma}')
    else:
        produto = 1
        for ordenada in l_ord:
            produto *= ordenada
        print(f'O produto das ordendas é: {produto}')

'''QUESTÃO 10: Dados dois números k e n como parâmetros, retorne uma lista com os primeiros k múltiplos de n.'''
def f_kMultiplos():
    n = int(0)
    i = int(0)
    l = list()
    
    #entrada de dados
    k = int(input("Quantos primeiros múltiplos: "))
    n = int(input("Múltiplos de quem?: "))
    
    l = []
    for i in range(1,k+1):
        resultado = i * n
        l.append(resultado)
    return l
    
def main():
    print(f_kMultiplos())
if __name__ == "__main__":
    main()
