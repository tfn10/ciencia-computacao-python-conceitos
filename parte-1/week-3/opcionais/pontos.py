"""Calcula a distância entre dois pontos em um plano cartesiano em duas dimensões.
Se a distância for maior ou igual 10, imprime 'longe', caso contrário, imprime 'perto'"""

x1 = int(input('Digite a coordenada de x1: '))
y1 = int(input('Digite a coordenada de y1: '))
x2 = int(input('Digite a coordenada de x2: '))
y2 = int(input('Digite a coordenada de y2: '))
distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
if distancia >= 10:
    print('longe')
else:
    print('perto')
