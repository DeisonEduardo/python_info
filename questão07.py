a = float(input(“1ª estatura: “)
b = float(input(“2ª estatura: “)
c = float(input(“3ª estatura: “)

if a == b or a == c or b == c:
      print(“Há, pelo menos, 2 pessoas com a mesma estatura”)
else:
      maior = max(a,b,c)
      print(“Maior estatura: “, maior)
