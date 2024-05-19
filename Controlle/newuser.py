import os
import sys
class NewUser():
    os.system('cls' if os.name == 'nt' else 'clear')

def data_new():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite seu nome: ")
    senha = input("Digite uma senha para sua conta: ")
    #tentar checar se a senha é válida
    data_nascimento = int(input("Digite sua data de nascimento: "))
    idade = int(input("Digite sua idade: "))
    cpf = int(input("Digite sua cpf: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Nome: " + nome)
    print("Senha: " + senha)
    print("Data de nascimento: " + str(data_nascimento))
    print("Idade: " + str(idade))
    print("CPF: " + str(cpf))

data_new()
verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

while verification != 0 and verification != 1:
    print("\n Opção Inválida. Por gentileza, escolha novamente.")
    verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

match verification:
    case 0:
        print("Conta Criada com Sucesso!")
        print("\nAguarde o prazo de até 8 dias para a aprovaçõa da sua conta.")
        print("\nA Santander agradeçe o sua confiança. Até logo.")
        sys.exit()
    case 1:
        data_new()