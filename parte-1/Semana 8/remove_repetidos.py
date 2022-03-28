def remove_repetidos(lista):
    """Remove os números repetidos de uma lista"""
    sem_duplicados = list()
    for numero in set(lista):
        # set() cria um conjunto sem os números duplicados:
        sem_duplicados.append(numero)
    return sorted(sem_duplicados)
