clientes = []


def cadastrar_cliente():
    print("================================")
    print("Cadastrar cliente")
    print("================================")
    print("")

    while True:
        codigo = input("Código do cliente: ")

        if codigo == "0":
            print()
            print("Você realmente quer cancelar o cadastro?")
            print()
            opcao = input("Digite 'S' para confirmar ou 'N' para continuar: ").upper()

            if opcao == "S":
                print()
                print("Cadastro de cliente cancelado.")
                print()
                return

            else:
                continue

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
        "endereco": endereco,
    }

    clientes.append(cliente)

    print()
    print(f"Cliente: {nome} código: {codigo} foi cadastrado com sucesso!")
    print()


def consultar_cliente():

    while True:
        codigo = input("Consultar Código: ")

        for cliente in clientes:
            if cliente["codigo"] == codigo:
                print()
                print(f"Código: {cliente['codigo']}")
                print(f"Razão Social: {cliente['nome']}")
                print(f"Nome do Responsável: {cliente['contato']}")
                print(f"Telefone: {cliente['telefone']}")
                print(f"Endereço: {cliente['endereco']}")
                print(f"Ativo: {'Sim' if cliente['ativo'] else 'Não'}")
                print()

                print("================================")
                print()

                while True:
                    opcao = input(
                        "Digite 1 para consultar outro cliente ou 0 para voltar: \n"
                    )
                    print()

                    if opcao == "0":
                        return

                    elif opcao == "1":
                        break

                break

        else:
            print()
            print(
                "Cliente não encontrado, por favor \n"
                "digite novamente o código do cliente."
            )
            print()


def listar_clientes():
    print("================================")
    print("Lista de Clientes")
    print("================================")
    print()
    for cliente in clientes:
        print(f"Código: {cliente['codigo']}")
        print(f"Razão Social: {cliente['nome']}")
        print(f"Nome do Responsável: {cliente['contato']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"Endereço: {cliente['endereco']}")
        print(f"Ativo: {'Sim' if cliente['ativo'] else 'Não'}")
        print("--------------------------------")


def alterar_cliente():
    while True:
        codigo = input("Alterar cliente - codigo: ")

        if codigo == "0":
            return

        for cliente in clientes:
            if cliente["codigo"] == codigo:
                print()
                print(f"Código: {cliente['codigo']}")
                print(f"Razão Social: {cliente['nome']}")
                print(f"Nome do Responsável: {cliente['contato']}")
                print(f"Telefone: {cliente['telefone']}")
                print(f"Endereço: {cliente['endereco']}")
                print(f"Ativo: {'Sim' if cliente['ativo'] else 'Não'}")
                print()

                while True:
                    opcao = input(
                        "================================ \n"
                        "O que deseja alterar? \n"
                        "  \n"
                        "1 - Razão Social \n"
                        "2 - Nome do Responsável \n"
                        "3 - Telefone \n"
                        "4 - Endereço \n"
                        "5 - Status \n"
                        "0 - Voltar \n"
                        "  \n"
                        "Escolha uma opção:"
                    )
                    print()

                    if opcao == "0":
                        return

                    elif opcao == "1":
                        print("Alterar Razão Social")
                        print()

                        while True:
                            nome_antigo = cliente["nome"]

                            novoNome = input("Insira nova razão social: \n").upper()

                            if novoNome == nome_antigo:
                                print()
                                print("Por favor digite uma razão social diferente")
                                print()

                            else:
                                cliente["nome"] = novoNome
                                print()
                                print("Razão Social Atualizada")
                                break

                    elif opcao == "2":
                        print("Alterar Nome do responsável")
                        print()

                        while True:
                            responsavel_antigo = cliente["contato"]

                            novoResponsavel = input(
                                "Insira novo responsável: \n"
                            ).upper()

                            if novoResponsavel == responsavel_antigo:
                                print()
                                print(
                                    "Por favor digite um nome diferente para o responsável"
                                )
                                print()

                            else:
                                cliente["contato"] = novoResponsavel
                                print()
                                print("Responsável Atualizado")
                                break

                    elif opcao == "3":
                        print("Alterar Telefone")
                        print()

                        while True:
                            telefone_antigo = cliente["telefone"]

                            while True:
                                novoTelefone = input("Insira novo telefone: \n")

                                novoTelefone = novoTelefone.replace("(", "")
                                novoTelefone = novoTelefone.replace(")", "")
                                novoTelefone = novoTelefone.replace("-", "")
                                novoTelefone = novoTelefone.replace(" ", "")

                                if not novoTelefone.isdigit():
                                    print()
                                    print("Telefone inválido.")
                                    print("Digite novamente.")
                                    print()
                                    continue

                                elif len(novoTelefone) == 8 or len(novoTelefone) == 9:
                                    novoTelefone = "11" + novoTelefone
                                    break

                                elif len(novoTelefone) == 10 or len(novoTelefone) == 11:
                                    break

                                else:
                                    print()
                                    print("Telefone inválido.")
                                    print("Digite novamente.")
                                    print()

                            if novoTelefone == telefone_antigo:
                                print()
                                print("Por favor digite um telefone diferente")
                                print()

                            else:
                                cliente["telefone"] = novoTelefone
                                print()
                                print("Telefone atualizado")
                                break

                    elif opcao == "4":
                        print("Alterar Endereço")
                        print()

                        while True:
                            endereco_antigo = cliente["endereco"]

                            novoEndereco = input("Insira novo endereço: \n").upper()

                            if novoEndereco == endereco_antigo:
                                print()
                                print("Por favor digite um endereço diferente")
                                print()

                            else:
                                cliente["endereco"] = novoEndereco
                                print()
                                print("Endereço atualizado")
                                break

                    elif opcao == "5":
                        print(
                            f"Status Atual: {'Ativo' if cliente['ativo'] else 'Inativo'}"
                        )
                        print()

                        while True:
                            opcao_status = input(
                                "Alterar Status \n"
                                "  \n"
                                "1 - Ativar cliente \n"
                                "2 - Desativar cliente \n"
                                "0 - Voltar \n"
                                "  \n"
                                "Escolha uma opção:"
                            )
                            print()

                            if opcao_status == "1":
                                cliente["ativo"] = True
                                print("Cliente Ativado com Sucesso.")
                                print()
                                break

                            elif opcao_status == "2":
                                cliente["ativo"] = False
                                print("Cliente Desativado com Sucesso.")
                                print()
                                break

                            elif opcao_status == "0":
                                break
        else:
            print()
            print(
                "Cliente não encontrado, por favor \n"
                "digite novamente o código do cliente."
            )
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
        print("0 - Voltar")
        print()

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == "1":
            cadastrar_cliente()
            print()

        elif opcao == "2":
            consultar_cliente()
            print()

        elif opcao == "3":
            listar_clientes()
            print()

        elif opcao == "4":
            alterar_cliente()
            print()

        elif opcao == "0":
            break

        else:
            print("Ops... Essa opção não existe.")
