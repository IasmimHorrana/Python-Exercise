#Exercise 28

#Descrição: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. (usando while)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

contador = 1
termo_atual = termo

while contador <= 10:
    print(termo_atual, end=' - ')
    termo_atual += razao
    contador += 1

print("ACABOU!")
