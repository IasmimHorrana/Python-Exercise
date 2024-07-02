#Exercise 13

#Peça ao usuario um número com casas decimais e informe a parte inteira desse número. 

import math

numero = float(input("Digite um número com casas decimais: "))
truncado = math.trunc(numero)
print(f"O número {numero} tem a parteira inteira {truncado}")

