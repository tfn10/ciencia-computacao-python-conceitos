def imprime_matriz(matriz):
    contador = 0
    for linha in matriz:
        for i in range(len(linha)):
            print(linha[i], end='')
            if i < (len(linha) - 1):
                print(end=' ')

        if contador < (len(matriz) - 1):
            print()
        contador += 1
