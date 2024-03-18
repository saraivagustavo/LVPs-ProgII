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

    while(i < len(l)):
        if(j == l[i]):
            n += 1
        i += 1

    return n

'''QUESTÃO 5: Dada uma lista de números, faça uma função que encontre e retorne o maior deles.'''
def f_maior(l):
    maior = l[0]

    for x in l:
        if(x > maior):
            maior = x

    return maior

'''QUESTÃO 6: Dada uma lista de números, faça um função que encontre e retorne o índice do maior deles.'''
def f_posicaoDoMaior(l):
    maior = int(0)
    i = int(0)
    i = 0
    maior_pos = f_maior(l)

    while(i < len(l)):
        if(maior_pos == l[i]):
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
    

    while(i < j):  
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

'''QUESTÃO 11: Faça um procedimento que leia um número n e depois a notas de n alunos (0 ≤ n ≤ 100). Em seguida, calcule e imprima a média da turma,e o número de alunos que ficaram com nota acima de 60.'''
def f_mediaAlunos(n,l):
    media = float(0.0)
    soma_notas = float(0.0)
    notas_maiores60 = float(0.0)

    soma_notas = 0
    nota_maior60 = 0
    if((n >= 0) and (n <= 100)):
        for notas in range(n):
            soma_notas += l[notas]
    
        for i in range(n):
            if(l[i] > 60):
                notas_maiores60 += 1

    media = soma_notas / n
    
    print(media)
    print(notas_maiores60)
        
'''QUESTÃO 12: Faça um procedimento que leia um número n e a temperatura de n dias do ano. Em seguida, calcule a média de temperatura anual e imprima o número de dias em que a temperatura ficou abaixo da média.'''
def f_mediaTemperaturas(n,l):
    media = float(0.0)
    soma_temps = float(0.0)
    temps_maioresMedia = float(0.0)

    soma_temps = 0
    temps_maioresMedia = 0
    for temperaturas in range(n):
        soma_temps += l[temperaturas]
    
    media = soma_temps / n

    for i in range(n):
        if(l[i] > media):
            temps_maioresMedia += 1
                
    print(temps_maioresMedia)

'''QUESTÃO 13: Dadas duas listas l1 e l2 com a mesma quantidade de números, imprima quantos elementos aparecem exatamente na mesma posiço em ambas as listas.'''
def f_mesmaPosicao(l1,l2):
    ocorrencia = int()

    ocorrencia = 0
    for i in range(len(l1)):
        if(l1[i] == l2[i]):
            ocorrencia += 1
    print(ocorrencia)

'''QUESTÃO 14: Dado um número n, faça um procedimento que leia o nome e o salário de n funcionários de uma empresa e imprima o nome de todos os funcionários que ganham mais que a média dos demais'''
def f_salarios(n,nome,salario):
    nomes_maisMedia = list()
    salario_total = float(0.0)
    media_salarial = float(0.0)

    salario_total = 0
    for x in range(n):
        salario_total += salario[x]

    media_salarial = salario_total / n

    for sujeito in range(n):
        if(salario[sujeito] > media_salarial):
            nomes_maisMedia.append(nome[sujeito])
    print(media_salarial)
    print(nomes_maisMedia)


'''QUESTÃO 15: Dada uma lista ordenada l e dois inteiros x e y(x < y), retorne uma sublista contendo todos os elementos de l que estiverem entre x e y'''
def f_sublista(l,x,y):
    subL = list()
    if(x < y):
        for valor in l:
            if((valor > x) and (valor < y)):
                subL.append(valor)
    return subL

'''QUESTÃO 16: Alice e Beatriz colecionam cartas de Pokémon. As cartas são produzidas para um jogo que reproduz a batalha introduzida em um dos mais bem sucedidos jogos de videogame da história, mas Alice e Beatriz são muito pequenas para jogar, e estão interessadas apenas nas cartas propriamente ditas. Para facilitar, vamos considerar que cada carta possui um identificador único que é um número inteiro. Cada uma das duas meninas possui um conjunto de cartas e, como a maioria das garotas de sua idade, gostam de trocar entre si as cartas que têm. Elas obviamente não tem interesse em trocar cartas idênticas, que ambas possuem, e não querem receber cartas repetidas na troca. Além disso, as cartas serão trocadas em uma única operação de troca: Alice da para Beatriz um sub-conjunto com N cartas distintas e recebe de volta um outro sub-conjunto com N cartas distintas. As meninas querem saber qual e o número máximo de cartas que podem ser tro- cadas. Por exemplo, se Alice tem o conjunto de cartas [1,1,2,3,5,7,8,8,9,15] e Beatriz o conjunto [2,2,2,3,4,6,10,11,11], elas podem trocar entre si no máximo quatro cartas. Escreva uma funcao que receba como parametros a lista de cartas que Alice tem e a lista de cartas que Beatriz possui, e imprima o número máximo de cartas que podem ser trocadas. As cartas de Alice e Beatriz são apresentadas em ordem não decrescente.'''
def f_semRepeticao(l):
    l2 = list()
       
    l2 = [l[0]]

    for i in l:
        if(i != l2[-1]):
            l2.append(i)
    return l2

def f_trocarCartas(l1,l2):
    n1 = int()
    n2 = int()

    l1 = f_semRepeticao(l1)
    l2 = f_semRepeticao(l2)

    n1 = 0
    for i in l1:
        if (i not in l2):
            n1 += 1

    n2 = 0
    for i in l2:
        if (i not in l1):
            n2 += 1

    return min(n1,n2)

'''#QUESTÃO 17: Dados m e n, crie e retorne uma matriz Mmxn nula.'''
def f_criaMatriz(m,n):
    M = []

    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(0)
        M.append(linha)
    
    return M

'''QUESTÃO 18: Dada uma matriz M, imprima esta matriz na tela.'''
def f_formataMatriz(M):
    for linha in M:
        for elemento in linha:
            print(elemento, end="\t")
        print()

'''QUESTÃO 19: Dadas duas matrizes A e B de mesmo tamanho, retorne uma terceira matriz com o resultado de A + B.'''
def f_somaMatriz(A,B):
    resultado = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] + B[i][j])
        resultado.append(linha)
        
    return resultado
'''QUESTÃO 20: Um professor deseja calcular o média de notas de uma turma. Faça um procedimento que leia uma matriz contendo as notas dos alunos. O procedimento começa perguntando o número "m" de alunos e número n de notas, e cria uma matriz "m x n" que armazena as "n" notas de cada um dos "m" alunos (os valores de "m", "n" e das notas serão lidos do teclado). A nota final de cada aluno é a média simples das suas "n" notas. O procedimento deve imprimir a nota de cada aluno, e no final a média geral da turma.'''
def f_lerNotas(m,n):
    alunos = []
    for i in range(m):
        notas = []
        for j in range(n):
            nota = int(input(f'Nota do aluno {i+1}: '))
            notas.append(nota)
        alunos.append(notas)
    return alunos
def f_mediaNotas():
    #declaração de variáveis
    m = int(0)
    n = int(0)
    somaAluno = float(0.0)
    somaTurma = float(0.0)
    mediaAluno = float(0.0)
    mediaTurma = float(0.0)
    #entrada de dados
    m = int(input("Quantos alunos: "))
    n = int(input("Quantas notas para cada aluno: "))
    #processamento
    alunos = f_lerNotas(m,n)
    somaTurma = 0
    for i in range(m):
        somaAluno = 0
        for nota in alunos[i]:
            somaAluno += nota
        mediaAluno = somaAluno / n
        somaTurma += mediaAluno
        print(f'Média do aluno {i+1}: {mediaAluno:.2f}')
    mediaTurma = somaTurma / m
    print(f'Média da turma: {mediaTurma:.2f}')

'''QUESTÃO 21: Dada uma matriz, verifique se ela é uma matriz identidade'''
def f_matrizIdentidade(M):
    linhas = len(M)
    colunas = len(M)
    for i in range(linhas):
        for j in range(colunas):
            if(i == j):
                if(M[i][j] != 1):
                    return False
            elif(M[i][j] != 0):
                    return False
    
    return True


'''QUESTÃO 22: Dada uma matriz M 3x3, calcule o determinante de M'''
def f_determinanteMatriz(M):
    diagonal_principal = int(0)
    diagonal_secundaria = int(0)
    determinante = 0
    for linha in range(3):
        diagonal_principal = 1
        diagonal_secundaria = 1
        for coluna in range(3):
            diagonal_principal *= M[coluna][(linha + coluna) % 3]
            diagonal_secundaria *= M[coluna][(linha - coluna) % 3]
        determinante += diagonal_principal - diagonal_secundaria
            
    return determinante


#testes
def main():
    M = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
    print(f_matrizIdentidade(M))

if __name__ == "__main__":
    main() 
