#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#Ordena as listas em ordem crescente
pares.sort()
impares.sort()

print(f"\nValores pares em ordem crescente: {pares}")
print(f"Valores ímpares em ordem crescente: {impares}")


