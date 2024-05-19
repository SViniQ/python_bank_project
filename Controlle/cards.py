import os
class Cards():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Aqui consta todos os cartões associados a sua conta.")

    def pickup():
        print("\nEscolha uma das opções abaixo: ")
        print("0 - Ver Cartões")
        print("1 - Adicionar Cartão")
        print("2 - Remover Cartão")
        print("3 - Voltar")

    pickup()
    choice = int(input("\nEscolha uma das opções acima: "))
    while choice != 0 and choice != 1 and choice != 2 and choice != 3:
        print("\nOpção Inválida. Por gentileza, escolha novamente.")
        choice = int(input("\nEscolha uma das opções acima: "))

    match choice:
        case 0:
            # Aqui será feito a busca dos cartões associados a conta do usuário
            # Tentar achar uma forma de fazer a busca dos cartões associados a conta do usuário no MySQL
            print("\nCartões associados a sua conta: ")
            print("Cartão de Crédito: 1234 5678 9012 3456")
            print("Cartão de Débito: 1234 5678 9012 3456")
            print("Cartão de Poupança: 1234 5678 9012 3456")
            verification = int(input("\nDeseja voltar ao menu iniciar ou voltar? (0 - MENU | 1 - VOLTAR): "))

            while verification != 0 and verification != 1:
                print("\n Opção Inválida. Por gentileza, escolha novamente.")
                verification = int(input("\nDeseja voltar ao menu iniciar ou voltar? (0 - MENU | 1 - VOLTAR): "))
 
            match verification:
                case 0:
                    from main import choices
                    main.choices()
                case 1: 
                    pickup()
        case 1:
            def add_card():
                # Aqui será feito a adição de um novo cartão a conta do usuário
                # Tentar achar uma forma de adicionar um novo cartão a conta do usuário no MySQL
                print("\nPreencha todos os dados abaixo: ")
                card_number = int(input("Infome o número do cartão: "))
                card_type = input("Informe o tipo do cartão: ")
                if card_type != "Crédito" and card_type != "Débito" and card_type != "Poupança" and card_type != "crédito" and card_type != "débito" and card_type != "poupança":
                    print("\nTipo de cartão inválido. Por gentileza, escolha entre Crédito, Débito ou Poupança.")
                    card_type = input("Informe o tipo do cartão: ")
                card_cvc = int(input("Informe o CVC do cartão: "))
                card_agency = int(input("Informe a agência do cartão: "))
                card_account = int(input("Informe a conta do cartão: "))
                card_expiration = int(input("Informe a data de vencimento do cartão: "))
            
                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n Número do Cartão: " + str(card_number))
                print("\n Tipo do Cartão: " + card_type)
                print("\n Data de Vencimento do Cartão: " + str(card_expiration))
                print("\n Código de Segurança (CVC): " + str(card_cvc))
                print("\n Conta do Cartão: " + str(card_account))
                print("\n Agência Vinculada ao Cartão: " + str(card_agency))

            add_card()
            verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

            while verification != 0 and verification != 1:
                print("\n Opção Inválida. Por gentileza, escolha novamente.")
                verification = int(input("\nTodos os dados acima estão corretos? (0 - SIM | 1 - NÃO): "))

            match verification:
                case 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    choice_user = int(input("\nCartão Adicionado com Sucesso. Deseja voltar ao menu iniciar ou voltar? (0 - MENU | 1 - VOLTAR):  "))
                    match choice_user:
                        case 0:
                            from main import choices
                            main.choices()
                        case 1:
                            pickup()
                case 1:
                    add_card()
        case 2:
            def remove_card():
                # Aqui será feito a remoção de um cartão associado a conta do usuário
                # Tentar achar uma forma de remover um cartão associado a conta do usuário no MySQL
                print("\nInforme o número do cartão que deseja remover: ")
                card_number = int(input("Número do Cartão: "))
                print("\nCartão removido com sucesso.")
            
            remove_card()
            print("\nCartão removido com sucesso.")
            verification = int(input("\nDeseja voltar ao menu iniciar ou voltar? (0 - MENU | 1 - VOLTAR): "))

            while verification != 0 and verification != 1:
                print("\n Opção Inválida. Por gentileza, escolha novamente.")
                verification = int(input("\nDeseja voltar ao menu iniciar ou voltar? (0 - MENU | 1 - VOLTAR): "))

            match verification:
                case 0:
                    from Controlle.main import choices
                    choices()
                case 1:
                    pickup()
        case 3:
            from main import choices
            main.choices()