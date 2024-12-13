def exibir_produtos(produtos):
    print("Produtos cadastrados:")
    for i in range(len(produtos)):
        print(f"Código: {i}, Descrição: {produtos[i][0]}, Preço: R${produtos[i][1]}")

produtos = [["Computador", 3000], ["Celular", 1500], ["Tablet", 800], ["Monitor", 1200]]

exibir_produtos(produtos)
