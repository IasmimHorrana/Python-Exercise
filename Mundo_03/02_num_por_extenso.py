#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros_por_extenso = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
    "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
    "Doze", "Treze", "Catorze", "Quinze", "Dezesseis",
    "Dezessete", "Dezoito", "Dezenove", "Vinte"
)

try:
    numero = int(input("Por favor, digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        #Acessa o elemento da tupla usando o número como índice
        print(f"O número {numero} por extenso é: {numeros_por_extenso[numero]}")
    else:
        print("Número fora do intervalo. Por favor, digite um número entre 0 e 20.")
except ValueError:
    print("Você não digitou um número válido. Por favor, tente novamente.")
