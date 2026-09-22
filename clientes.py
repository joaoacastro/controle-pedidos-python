clientes = []

def cadastrar_cliente():
    print("================================")
    print("Cadastrar cliente")
    print("================================")

    while True:
        codigo = input("Código do cliente: ")
        
        if not codigo.isdigit():
            print()
            print("Código inválido.")
            print("Digite novamente.")
            print()
            continue

        for cliente_existente in clientes:
            if cliente_existente["codigo"] == codigo:
                print()
                print(f"Cliente código {codigo} já está cadastrado!")
                print("Digite outro código para cadastrar o cliente.")
                print()
                break
        else:
            break

    nome = input("Razão Social: ").upper()
    contato = input("Nome do Responsável: ").upper()

    while True:
        telefone = input("Telefone: ")

        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace(" ", "")

        if not telefone.isdigit():
            print()
            print("Telefone inválido.")
            print("Digite novamente.")
            print()
            continue

        if len(telefone) == 8 or len(telefone) == 9:
            telefone = "11" + telefone
            break

        elif len(telefone) == 10 or len(telefone) == 11:
            break

        else:
            print()
            print("Telefone inválido.")
            print("Digite novamente.")
            print()


    endereco = input("Endereço: ").upper()

    cliente = {
        "codigo": codigo,
        "nome": nome,
        "contato": contato,
        "telefone": telefone,
        "ativo": True,
        "endereco": endereco
    }

    clientes.append(cliente)

    print()
    print(f"Cliente: {nome} código: {codigo} foi cadastrado com sucesso!")
    print()

def menu_clientes():
    while True:
        print()
        print("================================")
        print("           MENU CLIENTES")
        print("================================")
        print()
        print("1 - Cadastrar cliente")
        print("2 - Consultar cliente")
        print("3 - Listar clientes")
        print("4 - Alterar cliente")
        print("5 - Desativar clientes")
        print("0 - Voltar")
        print()

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == "1":
            cadastrar_cliente()
            print()
        elif opcao == "2":
            print("Consultar cliente")
        elif opcao == "3":
            print("================================")
            print("Lista de Clientes")
            print("================================")
            print()
            print(clientes)
        elif opcao == "4":
            print("Alterar cliente")
        elif opcao == "5":
            print("Desativar cliente")
        elif opcao == "0":
            break
        else:
            print("Ops... Essa opção não existe.")
