#Exercise 25

#Descrição: Crie um jogo onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

numero = random.randint(0, 10)
tentativas = 0

print("Estou pensando em um número entre 0 e 10. Tente adivinhar!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if palpite == numero:
        print(f"Parabéns! Você adivinhou o número {numero} em {tentativas} tentativas.")
        break
    elif palpite < numero:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
