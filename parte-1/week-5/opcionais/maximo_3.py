def maximo(n1, n2, n3):
    """Devolve o maior número"""
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n3 and n2 >= n1:
        return n2
    else:
        return n3
