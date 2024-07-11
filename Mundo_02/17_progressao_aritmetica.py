#Exercise 17

#Descrição: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao

for num in range(termo, decimo + 1, razao):
    print(num, end=' - ')
print("ACABOU!")
   