def inserir_jogador(jogadores):
    nome = input("Informe o nome do novo jogador: ")
    altura = float(input("Informe a altura do novo jogador (em metros): "))
    jogadores.insert(1, [nome, altura])  # Insere o jogador na segunda posição

    print("Lista de jogadores após a inserção:")
    print(jogadores)

jogadores = [["LeBron James", 2.06], ["Stephen Curry", 1.91], ["Kevin Durant", 2.06], ["Giannis Antetokounmpo", 2.11]]
# Chamada da função
inserir_jogador(jogadores)
