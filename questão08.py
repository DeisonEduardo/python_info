while True:  # Repete o programa todo até digitar 0
    print('''*** Calculadora de Números Reais ***
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
0. Sair''')
print("*" * 30)

    esc = int(input("Escolha a opção desejada: "))

    # Verifica se o usuário quer encerrar
    if esc == 0:
        print("Programa encerrado! Até logo.")
        break  # Interrompe o laço e fecha o programa

    # Verifica se a opção é uma operação válida
    if esc == 1 or esc == 2 or esc == 3 or esc == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if esc == 1:
            print(f'O resultado da conta: {n1} + {n2} = {n1 + n2}')
        elif esc == 2:
            print(f'O resultado da conta: {n1} - {n2} = {n1 - n2}')
        elif esc == 3:
            print(f'O resultado da conta: {n1} * {n2} = {n1 * n2}')
        elif esc == 4:
            if n2 != 0:
                print(f'O resultado da conta: {n1} / {n2} = {n1 / n2:.2f}')
            else:
                print("Erro. Divisão por zero!")
    else:
        print("Operação Inválida. Tente novamente!")

    print("-" * 30)  # Linha separadora entre operações
