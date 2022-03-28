"""Informa se um número é primo."""

numero = int(input('Digite um número inteiro: '))
contador = 1
divisores = 0
while contador <= numero:
    if numero % contador == 0:
        divisores += 1
    contador += 1
if divisores == 2:
    print('primo')
else:
    print('não primo')
