def menu_produtos():
    while True:
        print()
        print("================================")
        print("           PRODUTOS")
        print("================================")
        print()
        print("1 - Cadastrar produto")
        print("2 - Consultar produto")
        print("3 - Listar produtos")
        print("4 - Alterar produto")
        print("5 - Alterar disponibilidade")
        print("6 - Desativar produto")
        print("0 - Voltar")
        print()

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == "1":
            print("Cadastrar produto")
        elif opcao == "2":
            print("Consultar produto")
        elif opcao == "3":
            print("Listar produtos")
        elif opcao == "4":
            print("Alterar produto")
        elif opcao == "5":
            print("Alterar disponibilidade")
        elif opcao == "6":
            print("Desativar produto")
        elif opcao == "0":
            break
        else:
            print("Ops... Essa opção não existe.")