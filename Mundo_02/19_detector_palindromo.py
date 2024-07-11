#Exercise 19

#Descrição: Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase = input("Digite uma frase: ")

frase_sem_espacos = frase.replace(" ", "").lower()

# Verifica se a frase sem espaços é igual à sua reversão
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
