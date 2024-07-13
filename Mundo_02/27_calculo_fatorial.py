#Exercise 27

#Descrição: Faça um programa que leia um número qualquer e mostre seu fatorial ex: 5! = 5x4x3x2x1 = 120

from math import factorial #Usando o modulo

num = int(input("Digite um número para calcular o fatorial: "))
f = factorial(num)
print(f" O fatorial de {num} é {f}.")

#Sem o uso do modulo. 
numero = int(input("Digite um número para calcular o fatorial: "))

resultado = 1
contador = numero

sequencia = []

while contador > 1:
    resultado *= contador
    sequencia.append(contador)
    contador -= 1

sequencia.append(1)

sequencia_str = ' x '.join(map(str, sequencia))
print(f"{numero}! = {sequencia_str} = {resultado}")
