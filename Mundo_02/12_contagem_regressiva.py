#Exercise 12

#Descrição: Faça um programa que mostre na tela uma contagem regressiva indo de 10 a 0 com uma pausa de 0.5 segundo entre eles.

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("ACABOU!!")

