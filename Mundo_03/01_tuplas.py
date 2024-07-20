#1. Criar uma Tupla
frutas = ("Maçã", "Banana", "Laranja", "Uva", "Melancia")

print("Tupla de frutas:", frutas)

#2. Acessar Elementos da Tupla
primeira_fruta = frutas[0]
ultima_fruta = frutas[-1]

print(f"A primeira fruta é: {primeira_fruta}")
print(f"A última fruta é: {ultima_fruta}")

#3. Concatenar Tuplas
outras_frutas = ("Kiwi", "Abacaxi", "Manga")
todas_as_fruitas = frutas + outras_frutas

print("Tupla concatenada:", todas_as_fruitas)

#4. Iterar sobre a Tupla
print("Iterando sobre as frutas:")
for fruta in todas_as_fruitas:
    print(fruta)

#5. Desempacotar Tupla
primeira, segunda, terceira, quarta, quinta = frutas
print(f"Desempacotando a tupla: {primeira}, {segunda}, {terceira}, {quarta}, {quinta}")

