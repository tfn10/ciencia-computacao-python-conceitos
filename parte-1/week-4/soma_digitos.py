"""Imprime a soma dos dígitos de um número inteiro."""

numero = int(input('Digite um número inteiro: '))
soma_dos_digitos = 0
while numero > 0:
    ultimo_digito = numero % 10
    soma_dos_digitos += ultimo_digito
    numero = numero // 10
print(soma_dos_digitos)
