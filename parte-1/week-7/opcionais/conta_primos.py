def n_primos(numero):
    """Devolve quantos números primos existem entre 2 e 'n'"""
    numeros_primos = 0
    parametro = 2
    while parametro <= numero:
        if eh_primo(parametro):
            numeros_primos += 1
        parametro += 1
    return numeros_primos


def eh_primo(n):
    """Verfica se um número é primo"""
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
