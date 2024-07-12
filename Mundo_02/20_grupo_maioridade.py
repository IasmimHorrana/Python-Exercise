#Exercise 20

#Descrição: Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre as pessoas que atigiram a maioridade e as que são menores.

from datetime import date

# Obtém o ano atual
atual = date.today().year

# Inicializando contadores
maiores = 0
menores = 0

for pessoa in range(1, 8):
    nascimento = int(input("Digite o ano que a pessoa nasceu: "))
    idade = atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f"Total de pessoas maiores de idade: {maiores}")
print(f"Total de pessoas menores de idade: {menores}")
