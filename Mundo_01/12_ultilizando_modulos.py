#Exercise 12

#Descrição: ultilizando modulo math

#Primeira forma de importação:
import math 
numero = int(input("Digite um número: "))
raiz = math.sqrt(numero)

print(f"A raiz de {numero} é igual a {raiz:.2f}")

###

#Segunda forma de importação:
from math import sqrt 
numero = int(input("Digite um número: "))
raiz = sqrt(numero)

print(f"A raiz de {numero} é igual a {raiz:.2f}")
