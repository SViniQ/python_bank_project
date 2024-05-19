import os
import sys


class Payments():
    
    os.system('cls' if os.name == 'nt' else 'clear')

    def dados():
        barcode = int(input("Por gentileza informe o código do boleto: "))
        institution = input("Por gentileza informe a Instituição a receber o pagamento: ")
        amount = int(input("Por gentileza informe a quantidade de dinheiro que será transferida para o destinatário: "))

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n Código do Pagamento: " + str(barcode))
        print("\n Intituição destinatária: " + institution)
        print("\n Quantia a ser tranferida: " + str(amount))

    dados()

    verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

    while verification != 0 and verification != 1:
        print("\n Opção Inválida. Por gentileza, escolha novamente.")
        verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

    match verification:
        case 0:
            choice_user = int(input("Operação Realizada com Sucesso. Deseja retornar a tela incial? (0 - Retornar | 1 - Sair do Sistema): "))
            match choice_user:
                case 0:
                    from main import choices
                    main.choices()
                case 1:
                    print("\nA Santander agradeçe o sua confiança. Até logo!")
                    sys.exit()
        case 1: 
            dados()