#Exercise 27

#Descrição: Pergunte ao usuario a distancia da viagem em km e calcule o preço da passagem. Cobrando R$ 0.50 para viagens até 200km e R$ 0.45 para viagens mais longas.

distancia = float(input("Informe a distancia da viagem: "))

if distancia <= 200:
    km = distancia * 0.50
    print(f"O valor da viagem é: R$ {km}")
else:
    km = distancia * 0.45
    print(f"O valor da viagem é: R$ {km}")
