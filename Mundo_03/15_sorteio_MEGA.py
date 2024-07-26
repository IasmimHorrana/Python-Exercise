#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e 
#vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

print("Bem-vindo ao Gerador de Palpites da MEGA SENA!")
qtd_jogos = int(input("Quantos jogos você quer gerar? "))

palpites = []

for _ in range(qtd_jogos):
    jogo = sorted(random.sample(range(1, 61), 6))
    palpites.append(jogo)

print("\nPalpites Gerados:")
for i, jogo in enumerate(palpites, start=1):
    print(f"Jogo {i}: {jogo}")
