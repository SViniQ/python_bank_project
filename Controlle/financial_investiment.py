def main():
    print("Bem-vindo à página de investimentos!")
    print("Selecione uma opção:")
    print("1. Verificar saldo")
    print("2. Realizar um investimento")
    print("3. Visualizar histórico de investimentos")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        verificar_saldo()
    elif opcao == "2":
        realizar_investimento()
    elif opcao == "3":
        visualizar_historico()
    elif opcao == "4":
        print("Obrigado por usar nossa página de investimentos!")
    else:
        print("Opção inválida. Por favor, tente novamente.")

def verificar_saldo():
    # Lógica para verificar o saldo do usuário
    print("Seu saldo é de R$1000,00")

def realizar_investimento():
    # Lógica para realizar um investimento
    valor = float(input("Digite o valor do investimento: "))
    print(f"Investimento de R${valor} realizado com sucesso!")

def visualizar_historico():
    # Lógica para visualizar o histórico de investimentos
    print("Histórico de investimentos:")
    print("Investimento 1: R$500,00")
    print("Investimento 2: R$1000,00")

if __name__ == "__main__":
    main()