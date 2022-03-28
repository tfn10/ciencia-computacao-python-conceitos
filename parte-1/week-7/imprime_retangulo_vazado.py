largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
for alt in range(altura):
    for lar in range(largura):
        if alt != 0 and alt != (altura - 1) and lar != 0 and lar != (largura - 1):
            print(' ', end='')
        else:
            print('#', end='')
    print()
