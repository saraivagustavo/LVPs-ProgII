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

'''BOLÃO'''
import os

def limpaTela():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def listarJogadores(l):
	if len(l) > 0:
		print("Jogadores cadastrados:")
		
		for (nome, cpf) in l:
			print(nome, "-", cpf)
	else:
		print("Nenhum jogador cadastrado até agora.")
	
def nomeJog(jogs, cpf):
	for (n, c) in jogs:
		if c == cpf:
			return n
	
def existeCPF(c, l):
	for (nome, cpf) in l:
		if cpf == c:
			return True
	return False
	
def cadastrarJogador(l):
	listarJogadores(l)
	nome = input("Digite o nome do jogador: ")
	cpf = input("Digite o cpf do jogador: ")
	while existeCPF(cpf, l):
		print("Erro: CPF já existente.")
		cpf = input("Digite o cpf do jogador: ")
	l.append( (nome, cpf) )
	print("Jogador inserido com sucesso.")


def inserirNumerosApostados():
	l = []
	x = int(input("Quantos números neste bilhete? "))
	while x < 6 or x > 15:
		x = int(input("Ooops... digite um número entre 6 e 15: "))
	while len(l) < x:
		n = int(input("Digite um número: "))
		if n < 1 or n > 60 or n in l:
			print("Número inválido.")
		else:
			l.append(n)
	return l
	
def inserirCPFs(jogs):
	l = []
	listarJogadores(jogs)
	n = int(input("Quantos jogadores neste bilhete? "))
	for i in range(n):
		cpf = input("Digite o CPF do jogador: ")
		
		while not existeCPF(cpf, jogs):
			cpf = input("CPF inválido. Tente outro: ")
			
		l.append(cpf)
	return l
			
def cadastrarApostas(jogs, apostas):
	numeros = inserirNumerosApostados()
	cpfs = inserirCPFs(jogs)
	
	apostas.append( (numeros, cpfs) )
	print("Aposta cadastrada com sucesso.")

def listarApostas(jogs, apostas):
	for i in range(len(apostas)):
		numeros, cpfs = apostas[i]
		
		print(f'Bilhete {i+1}:')
		
		print('Números: ', end='')
		
		for n in numeros: print(n, end=' ')
		print()
		
		print('Jogadores:')
		for cpf in cpfs:
			print(nomeJog(jogs, cpf), '-', cpf)
		print()
			
def vencedora(aposta, sorteados):
	apostados = aposta[0]
	
	x = 0
	for n in apostados:
		if n in sorteados: x += 1
	return x == 6
	#########################
	#apostados = aposta[0]
	#
	#for n in sorteados:
	#	if n not in apostados: return False
	#
	#return True
	
def vencedoras(apostas, sorteados):
	l = []
	
	for aposta in apostas:
		if vencedora(aposta, sorteados):
			l.append(aposta)
	return l
	
def exibirVencedores(jogs, aposta, premioPorBilhete):
	cpfs = aposta[1]
	p = premioPorBilhete / len(cpfs)
	
	for cpf in cpfs:
		print(f'{nomeJog(jogs, cpf)} ({cpf}): R${p}')
	
def sorteio(jogs, apostas):
	sorteados = []
	while len(sorteados) < 6:
		x = int(input("Digite um número entre 1 e 60 que vc ainda não digitou: "))
		
		if x >=1 and x <= 60 and x not in sorteados:
			sorteados.append(x)
		else:
			print("Burrão")
	premioTotal = int(input("Digite o prêmio total: R$"))
	v = vencedoras(apostas, sorteados)
	limpaTela()
	if len(v) == 0:
		print("Não houve vencedores.")
	else:
		print("Apostas Vencedoras:")
		premioPorBilhete = premioTotal / len(v)
		
		i = 1
		for aposta in v:
			print(f'Bilhete {i}:')
			exibirVencedores(jogs, aposta, premioPorBilhete)
			print()
			i += 1

def main(args):
	print("Seja bem vindo ao Bolão")
	menu = '''
Escolha uma opção:

	1) Cadastrar jogador
	2) Visualizar jogadores cadastrados
	3) Cadastrar bilhete
	4) Visualizar bilhetes cadastrados
	5) Sorteio
	6) Sair
'''
	x = input(menu)
	jogs = []
	apostas = []
	while x != "6":
		limpaTela()
		if x == "1":
			cadastrarJogador(jogs)
		elif x == "2":
			listarJogadores(jogs)
		elif x == "3":
			cadastrarApostas(jogs, apostas)
		elif x == "4":
			listarApostas(jogs, apostas)
		elif x == "5":
			sorteio(jogs, apostas)
		else:
			print("Opção inválida. Tente novamente")
		x = input(menu)
	print("Tchau")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
	

'''GENIUS: '''
from random import randint
sorteado = randint(0,9)
correta = str(sorteado)

print(f'O primeiro número sorteado foi: {sorteado}')
x = input("Digite a sequência completa: ")
while(x == correta):
	sorteado = randint(0,9)
	correta += str(sorteado)
	limpaTela()
	print(f'O novo número é: {sorteado}')
	x = input("Digite a sequência completa: ")
	
print(f'Errou! Você acertou {len(correta)-1} números.')