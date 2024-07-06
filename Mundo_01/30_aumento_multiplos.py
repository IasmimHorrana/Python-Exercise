#Exercise 30

#Descrição: Pergunte o salario e calcule o valor do aumento. Salario superior a 1830 calcule o aumento de 10%, para inferior ou igual o aumento é de 15%.

salario_original = float(input("Informe o seu salario: "))

if salario_original > 1830:
    percentual = 0.10
else:
    percentual = 0.15

aumento = salario_original * percentual
valor_final = salario_original + aumento

print(f"Com o reajuste o seu salário de {salario_original} foi para R$: {valor_final}.")
