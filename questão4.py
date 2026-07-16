soma = 0
quantidade = 0
maior = 0

print("Digite números inteiros positivos. Para parar, digite um número negativo.")

while True:
    num = int(input("Digite um número: "))
    
    if num < 0:
        break 
    
    # se chegou aqui, é positivo
    soma += num
    quantidade += 1

    if quantidade == 1 or num > maior:
        maior = num

if quantidade > 0:
    media = soma / quantidade
    print(f"\nSoma dos números: {soma}")
    print(f"Média aritmética: {media:.2f}")
    print(f"O maior número informado: {maior}")
else:
    print("\nNenhum número positivo foi informado.")
