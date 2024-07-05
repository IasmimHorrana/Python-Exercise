#Exercise 26

#Descrição: Faça um programa que peça um número ao usuario e informa a ele se é par ou impar.

numero = int(input("Informe um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é IMPAR!")

