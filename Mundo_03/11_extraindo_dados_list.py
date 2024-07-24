#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

print("Digite números (digite 'fim' para parar):")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

#A) Quantos números foram digitados
print(f"\nTotal de números digitados: {len(numeros)}")

#B) Lista de valores ordenada de forma decrescente
numeros_ordenados = sorted(numeros, reverse=True)
print(f"Lista ordenada de forma decrescente: {numeros_ordenados}")

#C) Verifica se o valor 5 foi digitado e está na lista
valor_procurado = 5
if valor_procurado in numeros:
    print(f"O valor {valor_procurado} foi digitado e está na lista.")
else:
    print(f"O valor {valor_procurado} não foi digitado e não está na lista.")