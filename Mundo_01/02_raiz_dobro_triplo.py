#Exercise 2

#Descrição: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
print(f"O dobro de {numero} é: {dobro}, o triplo é: {triplo} e a raiz quadrada é: {raiz_quadrada:.2f}.")
