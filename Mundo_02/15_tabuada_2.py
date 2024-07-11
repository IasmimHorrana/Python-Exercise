#Exercise 15

#Descrição: Refazer a tabuada de um número que o usuario escolher utilizando o laço for. 

numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
