"""Imprime 'FizzBuzz' se o número for divisível por 3 e por 5"""

numero = int(input('Digite um número: '))
if numero % 3 == 0 and numero % 5 == 0:
    print('FizzBuzz')
else:
    print(numero)
