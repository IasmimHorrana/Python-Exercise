#Exercise 15

#Descrição: Calculando o seno, cosseno e tangente de um angulo qualquer. 

import math

angulo_graus = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo para radianos (pois as funções trigonométricas em Python usam radianos)
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno do ângulo: {seno:.2f}")
print(f"Cosseno do ângulo: {cosseno:.2f}")
print(f"Tangente do ângulo: {tangente:.2f}")
