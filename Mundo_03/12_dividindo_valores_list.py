#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter 
#apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
# Inicializa duas listas vazias

numeros = []
pares = []
impares = []

print("Digite números (digite 'fim' para parar):")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

print("\nLista Completa:")
print(numeros)

print("\nLista de Números Pares:")
print(pares)

print("\nLista de Números Ímpares:")
print(impares)
