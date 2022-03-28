"""Imprime os 'n' primeiros números ímpares naturais."""

n = int(input('Digite o valor de n: '))
impar = 1
while n > 0:
    print(f'{impar}')
    impar += 2
    n -= 1
