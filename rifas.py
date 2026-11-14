import random

nomes = []

quantidade = int(input("Quantas pessoas compraram a rifa? "))

for i in range(quantidade):
    nome = input("Digite o nome do comprador: ")
    nomes.append(nome)

ganhador = random.choice(nomes)

print("\nO ganhador da rifa foi:", ganhador)