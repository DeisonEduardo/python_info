produtos = []

resposta = "sim"

while resposta == "sim":
    produto = input("Digite o nome do produto: ")
    produtos.append(produto)

    resposta = input("Deseja adicionar outro produto? (sim/não): ")

print("\nLista de produtos:")
print(produtos)