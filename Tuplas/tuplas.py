'''QUESTÃO 1: A empresa pediu para você implementar uma sub-rotina que descubra qual é o funcionário com mais tempo de casa para lhe dar uma bonificação de 10% este mês (caso haja mais de um funcionário com este mesmo tempo de casa, todos eles receberão a bonificação). O procedimento a seguir recebe a lista de funcionários como parâmetro e imprime o nome do(s) funcionário(s) mais antigo(s) com seu salário diferenciado neste mês.'''
def f_bonusSalario(l):
    maiorTempo = 0
    for (_,tempo,_) in l:
        if(tempo > maiorTempo):
            maiorTempo = tempo
    for(nome,tempo,salario) in l:
        if(tempo == maiorTempo):
            print(f'{nome} vai receber R$: {salario*1.1:.2f}')

'''QUESTÃO 2: A mesma empresa deseja saber se seus produtos estão dando lucro. Para isso, pediu para você criar uma sub-rotina que recebe uma lista de tuplas contendo o preço de custo e o preço de venda de cada mercadoria e imprima:
a) a quantidade de produtos com menos de 20% de lucro
b) a porcentagem de produtos com lucro superior a 25%'''
def f_lucroProdutos(precos):
    menos20 = 0
    mais25 = 0
    for(custo, venda) in precos:
        if(venda < 1.2 * custo):
            menos20 += 1
        if(venda > 1.25 * custo):
            mais25 += 1
    print(f'a) {menos20} produto(s) está(ão) dando menos de 20% de lucro')
    print(f'b) {(mais25 / len(precos)) * 100} % dos produtos vendidos dão lucro superior a 25%')


'''QUESTÃO 3: Dada três tuplas representando pontos no plano cartesiano, verifique se os pontos estão alinhados.'''
#para saber se está alinhado, a determinante dos pontos é igual a zero.
def f_determinanteMatriz2(M):
    diagonalPrincipal1 = M[0][0] * M[1][1] * M[2][2]
    diagonalPrincipal2 = M[0][1] * M[1][2] * M[2][0]
    diagonalPrincipal3 = M[0][2] * M[1][0] * M[2][1]
    soma1 = diagonalPrincipal1 + diagonalPrincipal2 + diagonalPrincipal3

    diagonalSecundaria1 = M[0][2] * M[1][1] * M[2][0]
    diagonalSecundaria2 = M[0][0] * M[1][2] * M[2][1]
    diagonalSecundaria3 = M[0][1] * M[1][0] * M[2][2]
    soma2 = diagonalSecundaria1 + diagonalSecundaria2 + diagonalSecundaria3

    return soma1 - soma2

def f_pontosAlinhados(p1,p2,p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    M = [[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]]

    return f_determinanteMatriz2(M) == 0

'''QUESTÃO 4: Uma agência de turismo possui armazenados os voos realizados por diversas companhias aéreas. Cada voo é representado como uma tupla com as seguintes informações:
- Número do voo
- Companhia aérea (String)
- Escalas
EXEMPLO: voos = [(1024, "TAM", ["ES", "RJ", "SP", "NY"]), (1025, "GOL", ["ES", "SP"])]'''
'''A) Dados a lista de voo, cidade A e cidade B, imprima o número e a companhia de todos os voos que se iniciem em A e cujo destino é em B.'''
def f_rotas(voos,cidadeA,cidadeB):
    for (numero,companhia,escalas) in voos:
        if(escalas[0] == cidadeA.upper()) and (escalas[-1] == cidadeB.upper()):
            print(numero, companhia)

'''B) Dados a lista de voo, origem A e origem B, imprima quantos voos se iniciam em A e façam escala em B.'''
def f_escalas(voos,a,b):
    contador = 0
    for (_,_,escalas) in voos:
        if(escalas[0] == a.upper()) and b.upper() in escalas:
            contador += 1
    print(contador)

'''C) Dada a lista de voos, uma cidade origem A e uma cidade destino B, verifique se há algum voo direto de A para B, mesmo que A e B não sejam os destinos iniciais e finais do voo.'''
def f_vooDireto(voos,a,b):
    for(_,_,escalas) in voos:
        for i in range(len(escalas)-1):
            if(escalas[i] == a.upper()) and (escalas[i+1] == b.upper()):
                return True
    return False

'''QUESTÃO 5: Uma Copa do Mundo de futebol de botões está sendo realizada com times de todo o mundo. A classificação é baseada no número de pontos ganhos pelos times, e a distribuição de pontos é feita da forma usual. Ou seja, quando um time ganha um jogo, ele recebe 3 pontos; se o jogo termina empatado, ambos os times recebem 1 ponto; e o perdedor não recebe nenhum ponto. Dada a classificação atual dos times e o número de times participantes na Copa do Mundo, sua tarefa é criar uma função que determine quantos jogos terminaram empatados até o momento. A função deve receber dois parâmetros: o número de jogos já realizados até o momento e uma lista com a classificação atual. A classificação atual é dada por uma lista de tuplas, onde cada tupla contém o nome de um time e os pontos ganhos por aquele time.'''
def f_jogosEmpatados(N,l):
    soma = 0
    for (_,pontos) in l:
        soma += pontos
    resultado = 3*N - soma
    return resultado


def main():
    p1 = (1,2)
    p2 = (2,3)
    p3 = (3,4)
    print(f_pontosAlinhados(p1,p2,p3))
    

if __name__ == "__main__":
    main()