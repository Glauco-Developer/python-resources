def ordenar_jogadores_por_altura(jogadores, ordem='crescente'):
    jogadores_ordenados = jogadores[:]
    if ordem == 'crescente':
        for i in range(len(jogadores_ordenados)):
            for j in range(i + 1, len(jogadores_ordenados)):
                if jogadores_ordenados[i][1] > jogadores_ordenados[j][1]:
                    jogadores_ordenados[i], jogadores_ordenados[j] = jogadores_ordenados[j], jogadores_ordenados[i]
    elif ordem == 'decrescente':
        for i in range(len(jogadores_ordenados)):
            for j in range(i + 1, len(jogadores_ordenados)):
                if jogadores_ordenados[i][1] < jogadores_ordenados[j][1]:
                    jogadores_ordenados[i], jogadores_ordenados[j] = jogadores_ordenados[j], jogadores_ordenados[i]
    
    print("Jogadores ordenados por altura:")
    for i in range(len(jogadores_ordenados)):
        print(f"Código: {i}, Nome: {jogadores_ordenados[i][0]}, Altura: {jogadores_ordenados[i][1]} m")

jogadores = [["LeBron James", 2.06], ["Stephen Curry", 1.91], ["Kevin Durant", 2.06], ["Giannis Antetokounmpo", 2.11]]
# Chamada da função
ordenar_jogadores_por_altura(jogadores, ordem='decrescente')
