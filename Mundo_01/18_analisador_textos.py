#Exercise 18

#Descrição: Crie um programa que leia o nome completo de uma pessoa e mostre elas em maiusculas e minisculas, o total de letras e quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip()

print("Nome original:", nome)
print("Nome em maiúsculas:", nome.upper())
print("Nome em minúsculas:", nome.lower())
print("Total de letras (excluindo espaços):", len(nome) - nome.count(' '))
print("Total de letras do primeiro nome:", nome.find(' '))
