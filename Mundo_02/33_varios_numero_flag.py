#Exercise 33

#Descrição: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = 0
soma = 0

while True:
    numero = int(input("Digite um número (999 para parar): "))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f"Total de números digitados: {cont}")
print(f"Soma dos números digitados: {soma}")