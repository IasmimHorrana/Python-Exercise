#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

pessoas = []

while True:
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso (kg): "))
    pessoas.append((nome, peso))
    
    continuar = input("Deseja continuar? (S/N): ").lower()
    if continuar != 's':
        break

#Determina o número total de pessoas cadastradas
print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")

#Encontrar o maior e o menor peso
maior_peso = max(pessoas, key=lambda p: p[1])
menor_peso = min(pessoas, key=lambda p: p[1])

#Listagem das pessoas mais pesadas
print("\nPessoas mais pesadas:")
for pessoa in pessoas:
    if pessoa[1] == maior_peso[1]:
        print(f"{pessoa[0]} com {pessoa[1]} kg")

#Listagem das pessoas mais leves
print("\nPessoas mais leves:")
for pessoa in pessoas:
    if pessoa[1] == menor_peso[1]:
        print(f"{pessoa[0]} com {pessoa[1]} kg")
