def cadastrar_emprestimo():
    # Lógica para cadastrar um empréstimo
    pass

def listar_emprestimos():
    # Lógica para listar os empréstimos cadastrados
    pass

def buscar_emprestimo(id_emprestimo):
    # Lógica para buscar um empréstimo pelo ID
    pass

def atualizar_emprestimo(id_emprestimo):
    # Lógica para atualizar um empréstimo pelo ID
    pass

def excluir_emprestimo(id_emprestimo):
    # Lógica para excluir um empréstimo pelo ID
    pass

def menu():
    while True:
        print("----- MENU -----")
        print("1. Cadastrar empréstimo")
        print("2. Listar empréstimos")
        print("3. Buscar empréstimo")
        print("4. Atualizar empréstimo")
        print("5. Excluir empréstimo")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_emprestimo()
        elif opcao == "2":
            listar_emprestimos()
        elif opcao == "3":
            id_emprestimo = input("Digite o ID do empréstimo: ")
            buscar_emprestimo(id_emprestimo)
        elif opcao == "4":
            id_emprestimo = input("Digite o ID do empréstimo: ")
            atualizar_emprestimo(id_emprestimo)
        elif opcao == "5":
            id_emprestimo = input("Digite o ID do empréstimo: ")
            excluir_emprestimo(id_emprestimo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()