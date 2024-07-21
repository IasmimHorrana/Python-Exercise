#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, 
#mostre uma listagem de preços, organizando os dados em forma tabular.

produtos_precos = (
    ("Arroz", 7.50),
    ("Feijão", 9.30),
    ("Macarrão", 4.20),
    ("Leite", 5.80),
    ("Ovos", 8.45)
)

print('-' * 40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print('-' * 40)

for produto, preco in produtos_precos:
    print(f"{produto:.<30} R${preco:>7.2f}")







