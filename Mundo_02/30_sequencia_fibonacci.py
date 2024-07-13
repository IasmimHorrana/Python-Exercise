#Exercise 30

#Descrição: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

num = int(input("Digite o número de elementos da sequência de Fibonacci: "))

a = 0
b = 1

print(f"{a} - {b}", end=' - ')

contador = 2  

while contador < num:
    c = a + b
    print(c, end=' - ' if contador < num - 1 else '')
    a = b
    b = c
    contador += 1
print(" -> FIM")

