#Exercise 2

#Descrição: Faça um programa que leia um número inteiro e peça ao usuario para escolher a opção que deseja converter.

numero = int(input("Informe um número inteiro: "))

print("Escolha uma das bases para conversão:")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")

escolha = int(input("Informe aqui: "))

if escolha == 1:
    print(f"{numero} em BINÁRIO é {bin(numero)[2:]}")
elif escolha == 2:
    print(f"{numero} em OCTAL é {oct(numero)[2:]}")
elif escolha == 3:
    print(f"{numero} em HEXADECIMAL é {hex(numero)[2:]}")
else:
    print("Escolha inválida! Por favor, selecione 1, 2 ou 3.")






