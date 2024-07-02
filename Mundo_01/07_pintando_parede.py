#Exercise 7

#Descrição: Calcular quantos litros de tinta precisa para pintar uma parede.

largura = float(input("Digite o largura da parede: "))
altura = float(input("Digite o altura da parede: "))
metros_quadrados = largura * altura
litros_tinta = metros_quadrados / 2

print(f"Sua parede tem dimensão de: {largura:.2f}x{altura:.2f} e sua area é de {metros_quadrados:.2f}m²")
print(f"Para pintar essa parede você precisa de: {litros_tinta} litros de tinta.")
