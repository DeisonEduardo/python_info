tentativas = 0
usuario = input("Usuário: ")
senha = input("Senha: ")
tentativas = 1

while (usuario != "aluno" or senha != "12345") and tentativas < 3:
    print("Tente novamente")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    tentativas += 1

if usuario == "aluno" and senha == "12345":
    print("Acesso liberado")
else:
    print("Você tentou 3 vezes")
