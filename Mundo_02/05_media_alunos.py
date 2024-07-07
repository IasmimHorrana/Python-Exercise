#Exercise 5

#Descrição: Crie um programa que leia duas notas e calcule a media. Mostra msg de aprovado caso tenha tirado mais que 5 e reprovado caso tenha tirado menos.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"Com a nota {nota1} e a nota {nota2}, sua média é de: {media}")
    print("REPROVADO.")
elif 5 <= media < 6.9:
    print(f"Com a nota {nota1} e a nota {nota2}, sua média é de: {media}")
    print("RECUPERAÇÃO.")
else:
    print(f"Com a nota {nota1} e a nota {nota2}, sua média é de: {media}")
    print("APROVADO.")


