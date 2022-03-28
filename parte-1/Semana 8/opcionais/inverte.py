numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    numeros.append(n)
numeros.reverse()
print()
for numero in numeros:
    print(numero)
