# Exercício 4) Dada a lista valores = [34, 12, 5, 78, 23], 
# crie uma nova lista em ordem crescente e uma outra em ordem descrescente

valores = [34, 12, 5, 78, 23]
lista_ordenada_asc = sorted(valores)
lista_ordenada_desc = sorted(valores, reverse=True)

print(lista_ordenada_asc)
print(lista_ordenada_desc)
