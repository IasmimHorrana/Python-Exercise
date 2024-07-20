#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

# Ler quatro valores inteiros do teclado e armazená-los em uma tupla
valores = tuple(map(int, [input(f"Digite o valor {i+1}: ") for i in range(4)]))

print("Valores digitados:", valores)

quantidade_9 = valores.count(9)
print("O valor 9 apareceu:", quantidade_9, "vezes")

if 3 in valores:
    posicao_3 = valores.index(3) + 1
else:
    posicao_ = "O valor 3 não foi digitado."
print("O número 3 está na posição:", posicao_3)

numeros_pares = tuple(valor for valor in valores if valor % 2 == 0)
print("Números pares digitados:", numeros_pares)

