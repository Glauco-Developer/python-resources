# Gere os primeiros 10 numeros da sequencia Fibonacci e os imprima
a, b = 0, 1
count = 0
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1