Salário = float(input(“Salário: “)
Cargo = float(input(“Cargo: “)

if cargo == “Programador de sistemas”:
        salário = salário + salário * 0.30
elif cargo == “Analista de sistemas”:
        salário = salário + salário * 0.20
elif cargo == “Analista de banco”:
        salário = salário + salário * 0.15
else:
       print(“Cargo inválido!”)
       exit()
print(“Novo salário:”, salário)

