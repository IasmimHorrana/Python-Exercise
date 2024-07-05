#Exercise 24

#Descrição: Faça o computador pensar em um numero inteiro de 0 a 5 e peça para o usuario tentar adivinhar qual numero é. O programa vai mostrar na tela se o usuario venceu ou não.

from random import randint #Rodomizar numero inteiro
from time import sleep

print('-=-' * 17)
print("Vou pensar em um número de 0 e 5, tente adivinhar...")
print('-=-' * 17)

computador = randint(0,5)
numero = int(input("Em que número eu pensei? "))

print("PROCESSANDO..")
sleep(2)

if numero == computador:
    print("PARABÉNS!!! você acertou.")
else:
    print(f"QUE PENA!! eu pensei no {computador} e não {numero}.")

