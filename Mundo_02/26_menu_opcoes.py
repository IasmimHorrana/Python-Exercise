#Exercise 26

#Descrição: Crie um programa que leia dois valores e mostre um menu na tela. Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    print("\nDigite dois valores:")
    num1 = float(input("Primeiro valor: "))
    num2 = float(input("Segundo valor: "))
    
    while True:
        print("\n[ 1 ] somar")
        print("[ 2 ] multiplicar")
        print("[ 3 ] maior")
        print("[ 4 ] novos números")
        print("[ 5 ] sair do programa")
        
        escolha = int(input("Qual é a sua opção? "))
        
        if escolha == 1:
            soma = num1 + num2
            print(f"A soma de {num1} e {num2} é {soma}.")
        elif escolha == 2:
            produto = num1 * num2
            print(f"O produto de {num1} e {num2} é {produto}.")
        elif escolha == 3:
            if num1 > num2:
                print(f"O maior número entre {num1} e {num2} é {num1}.")
            elif num2 > num1:
                print(f"O maior número entre {num1} e {num2} é {num2}.")
            else:
                print(f"Os números {num1} e {num2} são iguais.")
        elif escolha == 4:
            break
        elif escolha == 5:
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
