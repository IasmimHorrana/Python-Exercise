#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado 
#e as suas respectivas posições na lista. 

valores = []

for i in range(5):
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

maior_valor = valores[0]
menor_valor = valores[0]
pos_maior = 0
pos_menor = 0

for i in range(len(valores)):
    if valores[i] > maior_valor:
        maior_valor = valores[i]
        pos_maior = i
    if valores[i] < menor_valor:
        menor_valor = valores[i]
        pos_menor = i

print(f"O maior valor digitado foi {maior_valor} na posição {pos_maior}.")
print(f"O menor valor digitado foi {menor_valor} na posição {pos_menor}.")
