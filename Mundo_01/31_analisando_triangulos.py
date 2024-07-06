#Exercise 31

#Descrição: Faça um programa que le o comprimento de três retas e diga ao usuario se pode formar um triangulo ou não. 

reta1 = float(input("Informe o comprimento da primeira reta: "))
reta2 = float(input("Informe o comprimento da segunda reta: "))
reta3 = float(input("Informe o comprimento da terceira reta: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("Com esses comprimentos é possível formar um triângulo.")
else:
    print("Com esses comprimentos não é possível formar um triângulo.")
