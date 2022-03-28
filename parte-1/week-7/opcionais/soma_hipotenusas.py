def soma_hipotenusas(n):
    """Devolve a soma de todas as hipotenusas entre 1 a 'n'"""
    parametro = 1
    soma_das_hipotenusas = 0
    while parametro <= n:
        if eh_hipotenusa(n):
            soma_das_hipotenusas += parametro
            print(parametro, end=' ')
        parametro += 1
    return soma_das_hipotenusas


def eh_hipotenusa(numero):
    """Verifica se um número tem hipotenusa"""
    for i in range(1, numero + 1):
        for j in range(1, numero + 1):
            if (i ** 2 + j ** 2) == (numero ** 2):
                return True
    return False
