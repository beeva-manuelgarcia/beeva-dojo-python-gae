__author__ = 'manuel'
### Ejercicio 1

from datetime import datetime
FORMATO = '%d/%m/%Y %H:%M:%S:%f'

def get_fecha():
    return datetime.now()

def ejercico(desde, hasta):
    multiplos = list()
    if desde>hasta:
        while desde >= hasta:
            if desde%7 == 0:
                multiplos.append(desde)
            desde -= 1
        return multiplos
    else:
        raise Exception

fecha = get_fecha()
print ('%s' % fecha.strftime(FORMATO))
multiplos = list()
multiplos=ejercico(2397, 2000)
for i in multiplos:
    print(i, end=";")
fecha = get_fecha()
print ('%s' % fecha.strftime(FORMATO))