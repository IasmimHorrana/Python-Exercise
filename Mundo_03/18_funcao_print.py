#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex: escreva('Olá, Mundo!')
#Saída:
#~~~~~~~~~
#Olá, Mundo!
#~~~~~~~~~

def escreva(texto: str):
    # Calcula o tamanho da borda
    tamanho_borda = len(texto) + 4
    borda = '~' * tamanho_borda
    
    # Exibe a mensagem formatada
    print(borda)
    print(f' {texto} ')
    print(borda)

# Exemplo de uso
escreva('Olá, Mundo!')
