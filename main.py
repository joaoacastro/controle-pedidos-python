from clientes import menu_clientes
from produtos import menu_produtos

def mostrar_menu_principal():
    print()
    print("================================")
    print("       CONTROLE DE PEDIDOS")
    print("================================")
    print()
    print("1 - Clientes")
    print("2 - Produtos")
    print("3 - Pedidos")
    print("0 - Sair")
    print()

while True:
    mostrar_menu_principal()

    opcao = input("Escolha uma opção: ")
    print()

    if opcao == "1":
        menu_clientes()
    elif opcao == "2":
        menu_produtos()
    elif opcao == "3":
        print("Pedidos")
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Ops...Opção inválida.")