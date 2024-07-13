#Exercise 31

#Descrição: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. No final, 
#mostre quantos números foram digitados e qual foi a soma entre eles.

contador = 0
soma = 0

numero = int(input("Digite um número (999 para parar): "))

while numero != 999:
    contador += 1
    soma += numero
    numero = int(input("Digite um número (999 para parar): "))

print(f"Total de números digitados: {contador}")
print(f"Soma dos números digitados: {soma}")
