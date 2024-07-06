#Exercise 4

#Descrição: Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele ainda vai se alistar ao serviço militar, se é a hora de
#se alistar ou se ja passou do tempo de alistamento. O programa deve mostrar o tempo que falta ou se passou do prazo.

from datetime import date

atual = date.today().year
nascimento = int(input("Informe o ano de nascimento: "))
idade = atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos.")

if idade == 18:
    print("Você precisa se alistar de imediato!")
elif idade < 18:
    falta = 18 - idade
    ano = atual + falta
    print(f"Ainda faltam {falta} anos para o alistamento.")
    print(f"Seu alistamento será em {ano}.")
elif idade > 18:
    falta = idade - 18
    ano = atual - falta
    print(f"Você deveria ter se alistado a {falta} anos.")
    print(f"Seu alistamento foi em {ano}.")