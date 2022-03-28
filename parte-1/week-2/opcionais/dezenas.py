"""Imprime o digito das dezenas de um número digitado"""

numero = int(input('Digite um número inteiro: '))
dois_ultimos_numeros = numero % 100
digito_das_dezenas = dois_ultimos_numeros // 10
print(f'O dígito das dezenas é {digito_das_dezenas}')
