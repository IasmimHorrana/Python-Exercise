#Exercise 18

#Descrição: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
divisores = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        divisores += 1

if divisores == 2:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
