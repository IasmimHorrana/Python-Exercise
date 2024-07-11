#Exercise 15

#Descrição: Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem par. Se o valor digitado for impar desconsidere
soma = 0
cont = 0

for num in range(1, 7):
    num = int(input("Digite um valor: "))
    if num % 2 ==0:
        soma = soma + num
        cont = cont + 1
print(f"Você informou {cont} números PARES e a soma foi {soma}.")
