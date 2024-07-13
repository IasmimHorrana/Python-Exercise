#Exercise 32

#Descrição: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
#qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
contador = 0
maior = menor = valor = 0

continuar = 'S'
while continuar in 'Ss':
    valor = int(input("Digite um número inteiro: "))
    
    soma += valor
    contador += 1
    
    if contador == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    
    continuar = input("Deseja continuar? [S/N] ")

if contador > 0:
    media = soma / contador
    print(f"Média dos valores: {media:.2f}")
    print(f"Maior valor digitado: {maior}")
    print(f"Menor valor digitado: {menor}")
else:
    print("Nenhum número foi digitado.")

print("Programa encerrado.")
