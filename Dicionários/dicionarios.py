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

def main():
    f_agenda()

if __name__ == "__main__":
    main()
