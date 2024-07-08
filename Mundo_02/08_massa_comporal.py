#Exercise 8

#Descrição: Faça um programa que calcule o IMC.

peso = float(input("Informe aqui o seu peso: "))
altura = float(input("Informe aqui sua altura: "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc <= 18.5:
    print("Você está abaixo do peso normal.")
elif imc <= 24.9:
    print("Você está no peso normal.")
elif imc <= 29.9:
    print("Você está com excesso de peso.")
elif imc <= 34.9:
    print("Você está com OBESIDADE de classe I.")
elif imc <= 39.9:
    print("Você está com OBESIDADE de classe II.")
else:
    print("Você está com OBESIDADE de classe III.")