import random
def gerar_lista_sem_duplicados(tamanho, inicio, fim):
    lista = []
    while len(lista) < tamanho:
        num = random.randint(inicio, fim)
        if num not in lista:
            lista.append(num)
    return lista

N = int(input("Digite o número de elementos: "))

# Criando a lista de elementos aleatórios sem duplicados
lista_aleatoria = []
while len(lista_aleatoria) < N:
    num_aleatorio = random.randint(10, 50)
    if num_aleatorio not in lista_aleatoria:
        lista_aleatoria.append(num_aleatorio)
# Criando a lista do usuário sem duplicados
lista_usuario = []
print("Agora, crie sua lista sem elementos duplicados.")

while len(lista_usuario) < N:
    num_usuario = int(input(f"Digite o elemento {len(lista_usuario) + 1} da lista (valor entre 10 e 50): "))
    if num_usuario not in lista_usuario and 10 <= num_usuario <= 50:  # Checar duplicados e intervalo
        lista_usuario.append(num_usuario)
    else:
        print("Número inválido ou duplicado. Tente novamente.")

print("Lista de elementos aleatórios únicos:", lista_aleatoria)
print("Lista criada pelo usuário sem duplicados:", lista_usuario)
