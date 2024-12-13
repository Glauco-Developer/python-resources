def exibir_jogadores(jogadores):
    print("Jogadores cadastrados:")
    for i in range(len(jogadores)):
        print(f"Código: {i}, Nome: {jogadores[i][0]}, Altura: {jogadores[i][1]} m")

jogadores = [["LeBron James", 2.06], ["Stephen Curry", 1.91], ["Kevin Durant", 2.06], ["Giannis Antetokounmpo", 2.11]]
exibir_jogadores(jogadores)
