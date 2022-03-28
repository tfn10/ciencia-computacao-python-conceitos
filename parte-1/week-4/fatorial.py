"""Calcula o fatorial de um numero natural."""

n = int(input('Digite o valor de n: '))
fatorial = 1
while n > 0:
    fatorial *= n
    n -= 1
print(f'{fatorial}')
