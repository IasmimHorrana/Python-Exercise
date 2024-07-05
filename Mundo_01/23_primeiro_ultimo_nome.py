#Exercise 23

#Descrição: Faça um programa que leia o nome de uma pessoa e informe a ela qual é o primeiro e ultimo nome dela. 

nome_completo = input("Digite seu nome completo: ").strip()

# Divide o nome completo em partes
nomes = nome_completo.split()

# O primeiro nome é o primeiro elemento da lista
primeiro_nome = nomes[0]

# O último nome é o último elemento da lista
ultimo_nome = nomes[-1]

print(f"Prazer em te conhecer {nome_completo}, tudo bem?")

print(f"Seu primeiro nome é: {primeiro_nome}")
print(f"Seu último nome é: {ultimo_nome}")
