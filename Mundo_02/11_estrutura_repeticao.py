#Exercise 11
#Descrição: Estrutura de repetição for

#Primeiro exemplo: 
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo:"))

for c in range(i, f+1, p):
    print(c)
print("Fim.")

#Segundo exemplo: 
for c in range(0, 5):
    n = int(input("Digite um valor: "))
print("Fim.")

#Terceiro exemplo:
soma = 0 
for c in range(0, 4):
    valor = int(input("Digite um valor: "))
    soma += valor
print(f"O somatório de tudo foi: {soma}")