#Exercise 19

#Descrição: Faça um programa que leia um numero de 4 digitos e determine qual é sua unidade, dezena, centena e milhar.

numero = int(input("Digite um número de até quatro dígitos: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)
