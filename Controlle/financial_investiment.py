import sys
class Financial_Investiment():
    print("Operação Indisponível no momento.")
    choice_user = int(input("\nDeseja retornar a tela incial? (0 - Retornar | 1 - Sair do Sistema) "))
    match choice_user:
        case 0:
            from main import choices
            main.choices()
        case 1:
            print("\nA Santander agradeçe o sua confiança. Até logo.")
            sys.exit()