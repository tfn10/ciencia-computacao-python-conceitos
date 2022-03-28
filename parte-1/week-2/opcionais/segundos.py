"""Imprime quantos dias, horas, minutos e segundos tem em uma quantidade de segundos"""

segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = segundos // 86400
segundos = segundos - dias * 86400
horas = segundos // 3600
segundos = segundos - horas * 3600
minutos = segundos // 60
segundos = segundos - minutos * 60
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')
