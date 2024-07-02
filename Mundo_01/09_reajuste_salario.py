#Exercise 8

#Descrição: Ler o salario de um funcionario e mostrar seu novo salario com 15% de aumento.

salario = float(input("Digite o seu salario: "))
novo_salario = salario + (salario * 15) / 100 

print(f"O valor do seu salario era de: R$ {salario} e com 15% de aumento fica: R$ {novo_salario:.2f}")
