__author__ = 'manuel'
### Ejercicio 1
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

multiplos = list()
multiplos=ejercico(2397, 2000)
for i in multiplos:
    print(i, end=";")
