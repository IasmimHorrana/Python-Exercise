#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e 
#também indique o menor e o maior valor que estão na tupla.

import random

#Gerar cinco números aleatórios e colocá-los em uma tupla
numeros_aleatorios = tuple(random.randint(1, 100) for _ in range(5))

#Mostrar a listagem de números gerados
print("Números gerados:", numeros_aleatorios)

menor_numero = min(numeros_aleatorios)
maior_numero = max(numeros_aleatorios)

print("Menor número na tupla:", menor_numero)
print("Maior número na tupla:", maior_numero)



