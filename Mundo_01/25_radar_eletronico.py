#Exercise 25

#Descrição: Escreva um programa que le a velocidade de um carro. Se ele ultrapassar a velocidade de 80km mostre a msg dizendo que ele foi multado. A muta vai custa 7,00 por cada km acima do limite.

velocidade_carro = float(input("Qual é a velocidade atual do carro? "))

if velocidade_carro > 80:
    print("MULTADO! você excedeu o limite da velocidade da via que é de 80km.")
    multa = (velocidade_carro-80) * 7
    print(f"Você deve pagar uma multa de: {multa}.")
else:
    print("Você está na velocidade permitida, tenha um bom dia.")
