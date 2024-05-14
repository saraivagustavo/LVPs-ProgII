'''QUESTÃO 1: Implemente uma função recursiva para calcular o fatorial de um número.'''
def f_fat(n):
    if(n == 0):
        return 1
    else:
        return n * f_fat(n-1)
    
'''QUESTÃO 2: Implemente uma função recursiva para calcular a soma de todos os elementos de uma lista.'''
def f_soma(l):
    if(len(l) == 0):
        return 0
    else:
        return l[0] + f_soma(l[:1])
    
'''QUESTÃO 3: Implemente uma funçãoo recursiva e outra iterativa para calcular o k-ésimo elemento da sequência de Fibonacci. Há alguma diferença significante no tempo de processamento das duas?'''
def f_fibonacci_recursivo(k): #a versão recursiva, a função se chama repetidamente até alcançar o caso base, resultando em múltiplas chamadas de função e uma árvore de chamadas recursivas.
    if(k <= 2):
        return 1
    else:
        return f_fibonacci_recursivo(k-1) + f_fibonacci_recursivo(k-2)
    
def f_fib_iterativo(k): #a versão iterativa, o cálculo é feito de forma sequencial, sem a necessidade de chamadas de função adicionais, armazenando os valores anteriores.
    x = 1
    y = 1
    for i in range(k-2):
        soma = x
        x = y
        y += soma
    return y

'''QUESTÃO 4: Implemente uma função recursiva para calcular o valor de x elevado a n.'''
def f_exponencial(x,n):
    if(n == 0):
        return 1
    else:
        return x * f_exponencial(x,n-1)
    
'''QUESTÃO 5: Implemente uma função recursiva para encontrar o maior elemento de uma lista'''
def f_maiorElemento(l):
    if(len(l) == 0):
        return l[0]
    else:
        maior = f_maiorElemento(l[1:])
        if(l[0] > m): return l[0]
        else: return m

'''QUESTÃO 6: Implemente uma função recursiva para calcular o Máximo Divisor Comum entre dois números.'''
def f_MDC(x,y):
    if(x%y == 0):
        return y
    else:
        return f_MDC(y,x%y)
    
'''QUESTÃO 7: Implemente uma função recursiva para imprimir ao contrário todos os algarismos de um número inteiro x.'''
def f_inverte(x):
    if(x < 10):
        print(x)
    else:
        print(x%10, end='')
        f_inverte(x//10)

'''QUESTÃO 8: Torre de Hanói, Considerando que as três torres se chamam, respectivamente, A, B e C, crie uma função recursiva para imprimir a menor sequência de passos necessária para mover n discos de A para B, podendo usar o auxílio de C. Regras:
(a) Só ́é possível mover um disco de cada vez.
(b) Um disco nunca pode ficar acima de outro disco menor que ele.'''
def f_hanoi(n,A,B,C):
    if(n == 1):
        print(f'{A} -> {B}')
    else:
        f_hanoi(n-1,A,C,B)
        f_hanoi(1,A,B,C)
        f_hanoi(n-1,C,B,A)

'''QUESTÃO 9: Implemente uma função recursiva que imprima QUAIS as permutações de n elemehtos de uma lista l.'''
def f_troca(l,x,y): #função de troca auxiliar na hora de chamar a função recursiva de permutações
    aux = l[x]
    l[x] = l[y]
    l[y] = aux

def f_permutacoes(l,pos = 0):
    if(pos == len(l)):
        print(l)
    else:
        for i in range(pos,len(l)):
            f_troca(l,i,pos) #fica o primeiro elemento da lista
            f_permutacoes(l,pos+1)
            f_troca(l,i,pos) #destrocar a primeira chamada da função f_troca(l,i,pos)

'''função main para casos de testes das funções'''
def main():
    l = [1,2,3]
    f_permutacoes(l)

if __name__ == "__main__":
    main()