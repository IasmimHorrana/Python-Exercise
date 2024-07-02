#Exercise 5

#Descrição: Lê um número inteiro do usuário e mostrar a tabuada.

numero = int(input("Digite um número inteiro: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
