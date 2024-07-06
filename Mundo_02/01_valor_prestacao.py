#Exercise 1

#Descrição: Faça um programa que aprova o emprestimo bancario para comprar uma casa. Pergunte o valor do imovel, o salario do usuario e em quantos anos ele vai pagar. 
#A prestação mensal não pode passar de 30% do salario ou então o emprestimo será negado.

casa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o seu salario: R$ "))
anos = int(input("Informe os anos de financiamento: "))

prestacao = casa / (anos * 12)
limite = salario * 30 / 100

if prestacao <= limite:
    print("Financiamento aceito.")
    print(f"O valor da prestação mensal é: R$ {prestacao:.2f}, que está dentro do limite de 30% do salário (R$ {limite:.2f}).")
else:
    print("Financiamento negado.")
    print(f"O valor da prestação mensal é: R$ {prestacao:.2f}, que excede o limite de 30% do salário (R$ {limite:.2f}).")


