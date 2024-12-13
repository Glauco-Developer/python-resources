def ordenar_por_preco(produtos):
    produtos_ordenados = produtos[:]
    for i in range(len(produtos_ordenados)):
        for j in range(i + 1, len(produtos_ordenados)):
            if produtos_ordenados[i][1] < produtos_ordenados[j][1]:
                produtos_ordenados[i], produtos_ordenados[j] = produtos_ordenados[j], produtos_ordenados[i]
    
    return produtos_ordenados

produtos = [["Computador", 3000], ["Celular", 1500], ["Tablet", 800], ["Monitor", 1200]]
produtos_por_preco = ordenar_por_preco(produtos)
print("Produtos ordenados por preço (mais caro para mais barato):")
for produto in produtos_por_preco:
    print(f"Descrição: {produto[0]}, Preço: R${produto[1]}")
