import random

N = int(input("Digite o número de elementos: "))

# Criando a lista de elementos aleatórios
lista_aleatoria = []
for _ in range(N):
    num_aleatorio = random.randint(10, 50)
    lista_aleatoria.append(num_aleatorio)

# Criando a lista a partir das entradas do usuário
lista_usuario = []
for i in range(N):
    num_usuario = int(input(f"Digite o elemento {i+1} da lista: "))
    lista_usuario.append(num_usuario)

print("Lista de elementos aleatórios:", lista_aleatoria)
print("Lista criada pelo usuário:", lista_usuario)


