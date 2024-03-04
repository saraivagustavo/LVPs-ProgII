'''1) FUNÇÃO PARA CALCULAR FATORIAL'''
def f_fat(n):
    if(n == 0):
        return 1
    else:
        return n * f_fat(n-1)
    
'''2) FUNÇÕES PARA CALCULAR COMBINAÇÃO (Cn,p = n!/p!*(n-p)!)'''
def f_combinacao(n,p):
    return f_fat(n) / (f_fat(p) * f_fat(n - p))

def f_combinacao2(n,p):
    numerador = f_fat(n)
    denominador = f_fat(p) * f_fat(n - p)
    return numerador / denominador

'''3) CRIE UM *PROCEDIMENTO* QUE IMPRIMA OS "N" PRIMEIROS MÚLTIPLOS DE K'''
def f_multiplos(n,k):
    #declaração de variáveis
    n = int(0)
    k = int(0)
    i = int(0)
    #entrada de dados e inicialização da variável
    n = int(input())
    k = int(input())
    i = 1
    #processamento
    if(n == 0):
        print(0)
    while(i <= n):
        print(i * k)
        i += 1

'''4) DADOS X E Y, VERIFIQUE SE X É DIVISOR DE Y'''
def f_divisor(x,y):
    num = int(input())
    deno = int(input())
    if(y % x == 0):
        return True
    else:
        return False

def f_divisor2(x,y):
    x = int(input())
    y = int(input())
    return y % x == 0

'''5) DADO N, IMPRIMA TODOS OS DIVISORES DE N'''
def f_divisores(n):
    n = int(input())
    i = 1
    while(i <= n):
        if(f_divisor(i,n)):
            print(i)
        i += 1 

'''6) DADOS X E Y, RETORNE O MAIOR DIVISOR COMUM ENTRE X E Y'''
def f_mdc(x,y):
    candidato += 1
    maior = 1
    while(candidato <= min(x,y)):
        if((f_divisor(candidato,n)) and (f_divisor(candidato,n))):
            maior = candidato
        candidato += 1
    print(maior)

'''7) DADO X, VERIFIQUE SE X É PRIMO'''
def f_primo(x):
    divisores = 0
    for i in range(1,x+1):
        if(x%i == 0):
            divisores += 1
        if(divisores == 2):
            return True
        else:
            return False
def f_primo2(x):
    if(x == 1):
        return False
    i = 2
    while(i < x):
        if(f_divisor(i,n)):
            return False
        i += 1
    return True

'''8) DADO N, IMPRIMA TODOS OS PRIMOS ATÉ N'''
def f_qntdprimos(n):
    for i in range(n,n+1):
        if(f_primo(i)):
            print(i)

def f_qntdprimos2(n):
    i = 2
    while(i <= n):
        if(f_primo(i)):
            print(i)
        i += 1

'''9) QUANTIDADE MINIMA DE MOVIMENTOS DA DAMA'''
def f_iguais(x1,y1,x2,y2):
    return (x1 == x2) and (y1 == y2)

def f_alinhados(x1,y1,x2,y2):
    return (x1 == x2) or (y1 == y2) or f_absoluto(x1 - x2) == f_absoluto(y1 - y2)

def f_absoluto(x)
    if(x > 0):
        return x
    else:
        return -x
    
def f_movimentosDama(x,y,m,n):
    if(f_iguais(x,y,m,n)):
        return 0
    if(f_alinhados(x,y,m,n)):
        return 1
    else:
        return 2  

'''10) ACEROLA'''
def f_acerola(N,F):
    frutas_colhidas = F * 0.05
    volumeL = frutas_colhidas /  N
    print(f'{volumeL:.2f}')

'''11) ALARME DESPERTADOR'''
def f_despertador(hora_atual,minuto_atual,hora_alarme,minuto_alarme):
    minutos_totais_atual =  hora_atual * 60 + minuto_atual
    minutos_totais_alarme = hora_alarme * 60 + minuto_alarme
    if(minutos_totais_atual > minutos_totais_alarme):
        print(24 * 60 + minutos_totais_alarme - minutos_totais_atual) #se o minuto atual é maior que o minuto do alarme, ela só acorda no próximo dia
    else:
        print(minutos_totais_alarme - minutos_totais_atual) #se for menor, ela acorda no mesmo dia                                   