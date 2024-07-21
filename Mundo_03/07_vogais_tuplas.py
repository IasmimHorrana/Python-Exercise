#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("banana", "maça", "uva", "abacaxi", "laranja")

#Iterar sobre cada palavra na tupla
for palavra in palavras:
    vogais = '' #Inicializar uma string para armazenar as vogais
    for letra in palavra:
        if letra in 'aeiou':
            vogais += letra + ' '
    print(f"As vogais da palavra {palavra} são: {vogais.strip()}")
