#Exercise 10

#Descrição: Jogo de pedra, papel e tesoura.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input("Escolha sua opção: "))

print(f"O computador escolheu {itens[computador]}.")
print(f"O jogador escolheu {itens[jogador]}.")

if jogador not in [0, 1, 2]:
    print("JOGADA INVÁLIDA!")
else:
    if computador == jogador:
        print("EMPATE")
    elif (computador == 0 and jogador == 1) or (computador == 1 and jogador == 2) or (computador == 2 and jogador == 0):
        print("JOGADOR VENCE")
    else:
        print("COMPUTADOR VENCE")


