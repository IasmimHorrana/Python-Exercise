#Exercise 22

#Descrição: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final o programa mostra:
#A media de idade do grupo, Qual o nome do homem mais velho, quantas mulheres tem menos de 20 anos. 

total_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
quantidade_mulheres_menos_20 = 0

for i in range(1, 5):
    print(f"--- Pessoa {i} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    total_idade += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        quantidade_mulheres_menos_20 += 1


media_idade = total_idade / 4

print("\nResultados:")
print(f"A média de idade do grupo é de {media_idade:.1f} anos.")
if nome_homem_mais_velho:
    print(f"O homem mais velho se chama {nome_homem_mais_velho} e tem {idade_homem_mais_velho} anos.")
else:
    print("Não há homens no grupo.")
print(f"Há {quantidade_mulheres_menos_20} mulher(es) com menos de 20 anos.")
