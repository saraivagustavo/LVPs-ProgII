'''QUESTÃO 1: Crie um dicionário com nome, idade e telefone de 10 pessoas (os dados serão digitados pelo usuário). Depois, remova todos os usuários que forem menores de idade, e imprima nome/telefone dos que permanecerem.'''
def f_maiorDeIdade():
    #declaração de variáveis
    agenda = {}
    i = int(0)
    nome = str('')
    idade = int(0)
    telefone = str('')
    #entrada de dados, processamento e saída de dados
    for i in range(3):
        nome = input(f"nome {i+1}: ")
        idade = int(input(f"idade {i+1}: "))
        telefone = input(f"telefone {i+1}: ")
        agenda[nome] = idade, telefone
        print()
        print(agenda)
    if ((agenda[nome][0]) < 18):
        del agenda[nome]
    print(f'agenda sem menor de idade {agenda}')

'''QUESTÃO 2: Faça um programa no qual o usuário possa armazenar o número de telefone de quantos contatos ele quiser. O programa tem um menu com duas opções:
• Cadastrar telefone: Usuário digita nome e telefone de um novo contato.
• Visualizar agenda: Programa exibe nomes e telefones cadastrados.'''
import os
def f_limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def f_agenda():
    #declaração de variáveis
    agenda = {}
    opcao = int(0)
    nome = str('')
    telefone = str('')
    #entrada de dados, processamento e saída de dados
    menu = '''
Escolha uma opção:
    1) Cadastrar nome e telefone
    2) Visualizar agenda
    3) Sair do programa
'''
    print(menu)
    opcao = int(input('Qual opção deseja?: '))
    f_limpaTela()
    while(opcao == 1 or opcao == 2 or opcao == 3):
        if(opcao == 1):
            nome = input('Digite o nome: ')
            telefone = input('Digite o telefone: ')
            agenda[nome] = telefone
        elif(opcao == 2 and len(agenda) == 0):
            print('Agenda vazia')
        elif(opcao == 3):
            print('Tchau!')
            break
        else:
            print(agenda)
        print(menu)
        opcao = int(input('Qual opção deseja?:  '))
        f_limpaTela()


'''QUESTÃO 3: Adapte o código do Bolão (lista de tuplas) para que os dados dos jogadores sejam salvos em um dicionário, ao invés de uma lista.'''
import os
def limpaTela():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def listarJogadores(jogadores):
	if len(jogadores) > 0:
		print("Jogadores cadastrados:")
		for cpf in jogadores:
			print(f'{jogadores[cpf]} (CPF: {cpf})')
	else:
		print("Nenhum jogador cadastrado até agora.")
	
def cadastrarJogador(jogadores):
	listarJogadores(jogadores)
	nome = input("Digite o nome do jogador: ")
	cpf = input("Digite o cpf do jogador: ")
	if cpf in jogadores:
		print("Erro: CPF já cadastrado no sistema.")
	else:
		print("Jogador inserido com sucesso.")
		jogadores[cpf] = nome
		
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
	
def inserirCPFs(jogadores):
	l = []
	listarJogadores(jogadores)
	n = int(input("Quantos jogadores neste bilhete? "))
	for i in range(n):
		cpf = input("Digite o CPF do jogador: ")
		while(cpf in l) or (cpf not in jogadores):
			cpf = input("CPF inválido. Tente outro: ")
		l.append(cpf)
	return l
			
def cadastrarApostas(jogadores, apostas):
	numeros = inserirNumerosApostados()
	cpfs = inserirCPFs(jogadores)
	
	apostas.append( (numeros, cpfs) )
	print("Aposta cadastrada com sucesso.")

def listarApostas(jogadores, apostas):
	for i in range(len(apostas)):
		numeros, cpfs = apostas[i]
		
		print(f'Bilhete {i+1}:')
		
		print('Números: ', end='')
		
		for n in numeros: print(n, end=' ')
		print()
		
		print('Jogadores:')
		for cpf in cpfs:
			print(jogadores[cpf])
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
	
def exibirVencedores(jogadores, aposta, premioPorBilhete):
	cpfs = aposta[1]
	p = premioPorBilhete / len(cpfs)
	
	for cpf in cpfs:
		print(f'{jogadores[cpf]} ({cpf}): R${p}')
	
def sorteio(jogadores, apostas):
	sorteados = []
	while len(sorteados) < 6:
		x = int(input("Digite um número entre 1 e 60 para ser sorteado: "))
		
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
			exibirVencedores(jogadores, aposta, premioPorBilhete)
			print()
			i += 1

def f_bolao():
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
	jogadores = {}
	apostas = []
	while x != "6":
		limpaTela()
		if x == "1":
			cadastrarJogador(jogadores)
		elif x == "2":
			listarJogadores(jogadores)
		elif x == "3":
			cadastrarApostas(jogadores, apostas)
		elif x == "4":
			listarApostas(jogadores, apostas)
		elif x == "5":
			sorteio(jogadores, apostas)
		else:
			print("Opção inválida. Tente novamente")
		x = input(menu)
	print("Tchau!")
	
def main():
    f_bolao()

if __name__ == "__main__":
    main()
