"""Verifica se o número recebido possui ao menos um digíto adjacente igual a ele"""

numero = int(input('Digite um número inteiro: '))
tem_adjacente = False
while numero > 0:
    ultimo_numero = numero % 10
    penultimo_numero = (numero // 10) % 10
    if ultimo_numero == penultimo_numero:
        tem_adjacente = True
        break
    numero = numero // 10

# só entra no 'if' caso tem_adjacente = True
if tem_adjacente:
    print('sim')
else:
    print('não')
