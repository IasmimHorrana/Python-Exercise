#Exercise 22

#Descrição: Faça um programa que leia a frase e: informe quantas vezes apareceu 'A', e a posição que aparece na primeira e ultima vez.

frase = str(input("Digite uma frase: ")).lower().strip()

# Conta quantas vezes a letra 'a' aparece na frase
contagem_a = frase.count('a')

# Encontra a posição da primeira letra 'a'
primeira_posicao = frase.find('a') + 1  # Adiciona 1 para ajustar para uma contagem humana (iniciando em 1)

# Encontra a posição da última letra 'a'
ultima_posicao = frase.rfind('a') + 1  

print(f"A letra 'A' aparece {contagem_a} vezes no texto.")
print(f'A letra "A" aparece a primeira vez na posição {primeira_posicao}')
print(f'A última letra "A" aparece na posição {ultima_posicao}')


