#Exercise 6

#Descrição: Programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.

from datetime import date

atual = date.today().year
nascimento = int(input("Informe o ano de nascimento: "))
idade = atual - nascimento


print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print("Categoria MIRIM.")
elif idade <= 14:
    print("Categoria INFANTIL.")
elif idade <= 19:
    print("Categoria JUNIOR.")
elif idade <= 25:
    print("Categoria SÊNIOR.")
else:
    print("Categoria MASTER.")

