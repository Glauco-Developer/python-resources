# Exercício 6) Dada a lista de listas 
# dados = [["Carlos", 23], ["Ana", 25], ["Pedro", 21], ["Beatriz", 24]]
#  faça o seguinte:

#a - Extraia apenas os nomes (no índice 0) de dados usando slice().
#b - Ordene esses nomes em ordem alfabética.
#c - Inverta a ordem dos nomes ordenados.
#d - Crie uma nova lista com os nomes ordenados usando sorted().
#e - Exiba cada nome junto com a idade correspondente.

#a
dados = [["Carlos", 23], ["Ana", 25], ["Pedro", 21], ["Beatriz", 24]]

nomes = [dado[0] for dado in dados] # solução pythônica

nomes_slice = nomes[0:4]
print(f"a) Nomes originais (slicing): {nomes_slice}")

#b
nomes.sort()
print(f"b) nomes ordenados: {nomes}")

#c
nomes.reverse()
print(f"c) nomes ordenados desc: {nomes}")

#d
nomes_ordenados = sorted(nomes_slice)
print(f"d) nomes ordenados com sorted: {nomes_ordenados}")

#e
print("e) Nomes e idades")
for dado in dados:
    print(f"{dado[0]}, Idade: {dado[1]}")
