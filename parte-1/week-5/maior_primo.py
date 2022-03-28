def maior_primo(numero):
    """Recebe um número maior ou igual a 2.
    Devolve o maior número primo menor ou igual ao número passado à função."""
    while numero > 2:
        if éPrimo(numero):
            return numero
        numero -= 1


def éPrimo(n):
    """Verifica se um número é primo."""
    contador = 1
    divisores = 0
    while contador <= n:
        if n % contador == 0:
            divisores += 1
        contador += 1
    if divisores == 2:
        return True
    else:
        return False
