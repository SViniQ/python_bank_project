import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Bem vindo ao Caixa Eletrônico do Santander.")

definition_user = int(input("\nNovo usuário? Faça seu cadastro aqui! (0 - Novo Usuário | 1 - Acesso Usuário): "))

while definition_user != 0 and definition_user != 1:
    print("\n Opção Inválida. Por gentileza, escolha novamente.")
    definition_user = int(input("\nNovo usuário? Faça seu cadastro aqui! (0 - Novo Usuário | 1 - Acesso Usuário): "))
    
match definition_user:
    case 0:
        from newuser import NewUser
        new_user = NewUser()
    case 1:
        from olduser import OldUser
        old_user = OldUser()

def choices():
    print("\nSegue abaixo suas possíveis escolhas: ")
    print("1 - Tranferências")
    print("2 - Pagamentos (CÓDIGO DE BARRAS)")
    print("3 - Cartãos")
    print("4 - PIX")
    print("5 - Empréstimos/Consignados")
    print("6 - Investimentos")
    print("7 - Falar com a Assistente Virtual")
    print("8 - Falar com um de nossos Atendentes")
    print("9 - Sair")

choices()
match_user = int(input("\nEscolha uma das operações que deseja realizar: "))

match match_user:
    case 1:
        from Controlle.transfers import Transfers
        transfers = Transfers()
    case 2:
        from Controlle.payments import Payment
        payment = Payment()
    case 3:
        from Controlle.cards import Cards
        cards = Cards()
    case 4:
        from Controlle.pix import PIX
    case 5:
        from Controlle.lendings import Lendings
    case 6:
        from Controlle.financial_investiment import Investiment
    case 7:
        from Controlle.AI import AI
    case 8:
        from Controlle.your_team import YourTeam
    case 9:
        from Controlle.exit import Exit