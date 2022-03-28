"""Imprime 'Fizz' se o número digitado for divisível por 3"""

numero = int(input('Digite um número: '))
if numero % 3 == 0:
    print('Fizz')
else:
    print(numero)
