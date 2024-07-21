#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

valores = []

while True:
    valor = int(input("Digite um valor (ou -1 para parar): "))
    
    if valor == -1:
        break
    
    if valor not in valores:
        valores.append(valor)

valores.sort() #Ordenar a lista em ordem crescente

print("Valores únicos digitados, em ordem crescente:")
print(valores)
