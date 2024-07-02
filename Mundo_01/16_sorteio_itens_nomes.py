#Exercise 16

#Descrição: Sorteando um nome aleatorio. 
import random

nome1 = str(input("Nome da primeira integrante: "))
nome2 = str(input("Nome da segunda integrante: "))
nome3 = str(input("Nome da terceira integrante: "))
nome4 = str(input("Nome da quarta integrante: "))
nome5 = str(input("Nome da quinta integrante: "))
nome6 = str(input("Nome da sexta integrante: "))
nome7 = str(input("Nome da setima integrante: "))

lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7]
escolhida = random.choice(lista)
print(f"A integrante escolhida é: {escolhida}.")





