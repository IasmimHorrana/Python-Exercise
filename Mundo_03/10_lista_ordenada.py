#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
#No final, mostre a lista ordenada na tela.

numeros = []

for c in range(5):
    valor = int(input("Digite um valor numérico: "))
    
    #Encontra a posição correta para inserir o valor
    posicao = 0
    while posicao < len(numeros) and numeros[posicao] < valor:
        posicao += 1
    #Insere o valor na posição correta
    numeros.insert(posicao, valor)

print("Lista ordenada:", numeros) #Exibe a lista ordenada
