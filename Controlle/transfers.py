import sys
import os

class Transfers():
    
    os.system('cls' if os.name == 'nt' else 'clear')

    def dados():
        os.system('cls' if os.name == 'nt' else 'clear')
        account = input("Por gentileza informe o nome do destinatário da transferência: ")
        cpf = int(input("Por gentileza informe o CPF do destinatário: "))
        amount = int(input("Por gentileza informe a quantidade de dinheiro que será transferida para o destinatário: "))

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n Destinatário da Transferência: " + account)
        print("\n CPF do Destinatário " + str(cpf))
        print("\n Quantia a ser tranferida: " + str(amount))

    dados()

    verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

    while verification != 0 and verification != 1:
        print("\n Opção Inválida. Por gentileza, escolha novamente.")
        verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))
 
    match verification:
        case 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            choice_user = int(input("\nOperação Realizada com Sucesso. Deseja retornar a tela incial? (0 - Retornar | 1 - Sair do Sistema) "))
            match choice_user:
                case 0:
                    from main import choices
                    main.choices()
                case 1:
                    print("\nA Santander agradece o sua confiança. Até logo.")
                    sys.exit()
        case 1: 
            dados()

transferencia = Transfers()
transferencia.dados()