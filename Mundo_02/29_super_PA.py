#Exercise 29

#Descrição: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. 
# (usando while e criando um laço)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
total = 0
mais = 10

contador = 1
termo_atual = termo
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo_atual, end=' - ')
        termo_atual += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos tempos você quer mostrar mais? "))
print(f"Progressão finalizado com {total} termos mostrados.")
