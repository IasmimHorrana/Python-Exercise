#Exercise 7

#Descrição: Faça um programa que peça os 3 lados do triangulo e informe se é equilatero, isosceles ou escaleno.

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados formam um triângulo ", end='')

    if lado1 == lado2 == lado3:
        print("EQUILÁTERO.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("ISÓSCELES.")
    else:
        print("ESCALENO.")
else:
    print("Os lados não formam um triângulo.")
