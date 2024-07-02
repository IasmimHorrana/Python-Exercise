#Exercise 11

#Descrição: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quantidade_km = float(input("Informe quantos km percorridos com o carro alugado: "))
quantidade_dias = float(input("Informe quantos dias o carro ficou alugado: "))
aluguel = (quantidade_dias * 60) + (quantidade_km *0.15)

print(f"O total a pagar é: R$ {aluguel}")
