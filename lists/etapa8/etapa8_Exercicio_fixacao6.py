def ordenar_produtos_por_quantidade(produtos, ordem='crescente'):
    produtos_ordenados = produtos[:]
    if ordem == 'crescente':
        for i in range(len(produtos_ordenados)):
            for j in range(i + 1, len(produtos_ordenados)):
                if produtos_ordenados[i][1] > produtos_ordenados[j][1]:
                    produtos_ordenados[i], produtos_ordenados[j] = produtos_ordenados[j], produtos_ordenados[i]
    elif ordem == 'decrescente':
        for i in range(len(produtos_ordenados)):
            for j in range(i + 1, len(produtos_ordenados)):
                if produtos_ordenados[i][1] < produtos_ordenados[j][1]:
                    produtos_ordenados[i], produtos_ordenados[j] = produtos_ordenados[j], produtos_ordenados[i]
    
    print("Produtos ordenados por quantidade disponível:")
    for i in range(len(produtos_ordenados)):
        print(f"Código: {i}, Descrição: {produtos_ordenados[i][0]}, Preço: R${produtos_ordenados[i][1]}")

produtos = [["Computador", 3000], ["Celular", 1500], ["Tablet", 800], ["Monitor", 1200]]     
# Exemplo de chamada da função
ordenar_produtos_por_quantidade(produtos, ordem='crescente')