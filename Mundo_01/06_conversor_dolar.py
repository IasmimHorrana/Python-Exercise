#Exercise 6

#Descrição: Conversor de real para quantos USD você consegue comprar. 

moeda  = float(input("Digite o valor em real: "))
conversor = moeda / 5.66
print(f"Com esse dinheiro você pode comprar: $ {conversor:.2f} dolares.")