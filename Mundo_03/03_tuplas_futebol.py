#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time do São Paulo.

times_campeonato_brasileiro_2024 = (
    "América-MG", "Athletico-PR", "Atlético-MG", "Bahia", 
    "Botafogo", "Corinthians", "Coritiba", "Cruzeiro", 
    "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", 
    "Goiás", "Grêmio", "Internacional", "Palmeiras", 
    "Red Bull Bragantino", "Santos", "São Paulo", "Vasco da Gama"
)

#Os 5 primeiros times
primeiros_cinco = times_campeonato_brasileiro_2024[:5]
print("Os 5 primeiros times:")
print(primeiros_cinco)

#Os últimos 4 colocados
ultimos_quatro = times_campeonato_brasileiro_2024[-4:]
print("Os últimos 4 colocados:")
print(ultimos_quatro)

#Times em ordem alfabética
lista_times_ordenada = sorted(times_campeonato_brasileiro_2024)
print("Times em ordem alfabética:")
print(lista_times_ordenada)

#Em que posição está o time do São Paulo
posicao_sao_paulo = times_campeonato_brasileiro_2024.index("São Paulo") + 1
print(f"O time do São Paulo está na posição {posicao_sao_paulo}.")
