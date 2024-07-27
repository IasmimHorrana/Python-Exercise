#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}

nome = input("Digite seu nome: ")
media = float(input("Digite sua média: "))

if media >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#Adicionando informações ao dicionário
aluno["nome"] = nome
aluno["media"] = media
aluno["situacao"] = situacao

print("\nDados do Aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

    
