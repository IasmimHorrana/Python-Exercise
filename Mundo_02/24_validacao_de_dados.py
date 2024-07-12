#Exercise 24

#Descrição: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente.

sexo = input("Digite o seu sexo (M/F): ").strip().upper()

while sexo != 'M' and sexo != 'F':
    print("Entrada inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")
    sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()

print(f"Sexo '{sexo}' registrado com sucesso.")
