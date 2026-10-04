logado = False
usuario_logado = ""

while True:
    print("\033c", end="")
    print("#########################################")
    print("SISTEMA DE CADASTRO DE USUÁRIOS")
    print("#########################################\n")

    if not logado:
        print("===LOGIN===""")
        login = (input("Digite seu login: "))
        senha = (input("Digite sua senha: "))

        if login =="admin" and senha =="123":
            print(f"Login realizado com sucesso! Bem-vindo, {login}!.\n")
            input("ENTER para continuar...")
            logado = True
            usuario_logado = login 
        else:
            input("\nLogin ou senha incorretos! ENTER para tentar novamente.")

    else:
        print("===MENU PRINCIPAL===""")
        print(f"Usuário logado: {usuario_logado}")
        print("1 - Inserir usuário")
        print("2 - Pesquisar usuário")
        print("3 - Remover usuário")
        print("4 - Listar todos os usuários")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Fazendo logout...")
            input("ENTER para voltar para o login.")
            logado = False

        elif opcao == "6":
            print("Encerrando o sistema... Até logo!")
            break

        elif opcao in ["1", "2", "3", "4"]:
            input("Em Desenvolvimento. ENTER para continuar...")

        else:
            input("Opção inválida! ENTER para continuar...")