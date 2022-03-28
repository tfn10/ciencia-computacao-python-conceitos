"""Imprime 'Buzz' se o número for divisível por 5"""

numero = int(input('Digite um número: '))
if numero % 5 == 0:
    print('Buzz')
else:
    print(numero)
