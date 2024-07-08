#Exercise 9

#Descrição: Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço e sua forma de pagamento.
#á vista tem 10% de desconto
#á vista cartão tem 5% de desconto
#em até 2x no cartão fica o preço normal
#3x ou mais no cartão fica 20% de juros.

valor = float(input("Preço das compras: R$ "))

print("FORMA DE PAGAMENTO:")
print("[1] à vista dinheiro ou pix")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

escolha = int(input("Qual é a opção? "))

if escolha == 1:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"O valor da compra com desconto de 10% fica de R${valor:.2f} por R${valor_final:.2f}.")
elif escolha == 2:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print(f"O valor da compra com desconto de 5% fica de R${valor:.2f} por R${valor_final:.2f}.")
elif escolha == 3:
    parcela = valor / 2
    print(f"O valor da compra será parcelado em 2x de R${parcela:.2f}. Total: R${valor:.2f}.")
elif escolha == 4:
    parcelas = int(input("Quantas parcelas? "))
    if parcelas > 2:
        juros = valor * 0.20
        valor_final = valor + juros
        parcela = valor_final / parcelas
        print(f"Sua compra será parcelada em {parcelas}x de R${parcela:.2f} com juros. Total: R${valor_final:.2f}.")
    else:
        print("Número de parcelas inválido. Deve ser 3 ou mais.")
else:
    print("Opção inválida.")
