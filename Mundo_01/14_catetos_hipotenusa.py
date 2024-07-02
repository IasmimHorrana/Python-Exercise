#Exercise 14

#Descrição: Calculo da hipotenusa:

import math

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

# Calculando a hipotenusa usando o Teorema de Pitágoras
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

print(f"A hipotenusa é: {hipotenusa:.2f}")






