notas = []

while True:
    nota = float(input("Digite uma nota (ou -1 para parar): "))
    if nota == -1:
        break
    notas.append(nota)

if len(notas) > 2:
    notas.sort()
    notas_intermediarias = notas[1:-1]  # Excluir a menor e a maior nota
    media = sum(notas_intermediarias) / len(notas_intermediarias)
    print(f"A média das notas descartando a menor e a maior é: {media:.2f}")
else:
    print("Notas insuficientes para calcular a média excluindo a menor e a maior.")
    