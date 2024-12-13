def inserir_produto(produtos):
    descricao = input("Informe a descrição do novo produto: ")
    preco = float(input("Informe o preço do novo produto: "))
    produtos.insert(1, [descricao, preco])  # Insere o produto na segunda posição

    print("Lista de produtos após a inserção:")
    print(produtos)

produtos = [["Computador", 3000], ["Celular", 1500], ["Tablet", 800], ["Monitor", 1200]]
# Chamada da função
inserir_produto(produtos)
