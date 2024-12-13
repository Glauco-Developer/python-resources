def ordenar_por_altura(jogadores):
    jogadores_ordenados = jogadores[:]
    for i in range(len(jogadores_ordenados)):
        for j in range(i + 1, len(jogadores_ordenados)):
            if jogadores_ordenados[i][1] < jogadores_ordenados[j][1]:
                jogadores_ordenados[i], jogadores_ordenados[j] = jogadores_ordenados[j], jogadores_ordenados[i]
    
    return jogadores_ordenados

jogadores = [["LeBron James", 2.06], ["Stephen Curry", 1.91], ["Kevin Durant", 2.06], ["Giannis Antetokounmpo", 2.11]]
jogadores_por_altura = ordenar_por_altura(jogadores)
print("Jogadores ordenados por altura (mais alto para mais baixo):")
for jogador in jogadores_por_altura:
    print(f"Nome: {jogador[0]}, Altura: {jogador[1]} m")
    