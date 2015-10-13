__author__ = 'manuel'
from random import randint

DIAS = int(7)
HORAS = int(24)
VILLANOMAX = int(3)
SEMANA = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabados', 'Domingo']



def generarVillanos2(numeroVillanos):
	villanos = [ ]
	for i in range(numeroVillanos):
		villanos.append(['Villano' + str(i), randint(1, 30), randint(1000, 3000), randint(1, 10), randint(0, 1)])
	return villanos


def pintarVillanos(villanos):
	print '[Nombre, Vida, Recompensa, Distancia, Villano]'
	for i in range(len(villanos)):
		print villanos[i]


def ordenarVillanos(villanos):
	villanosOrd = villanos
	villanosOrd.sort(lambda x,y: cmp(x[3],y[3]))
	return villanosOrd


def esVillano(villano):
	if int(villano[4]) == int(1):
		return True
	else:
		return False


def main():
	villanos = generarVillanos2(randint(5, 10))
	pintarVillanos(villanos)

	#ordenamos villanos por distancia para ir a por ellos
	villanosOrd = ordenarVillanos(villanos)
	#print villanosOrd

	villanoNum = 0
	horasTotales = int(0)
	gananciasTotales = int(0)
	for i in range(DIAS):
		print 'Dia: ', int(i + 1), ' ', SEMANA[i]
		for j in range(HORAS):
			if esVillano(villanosOrd[villanoNum]):
				horasTotales +=1
				print 'Hora: ', j, 'Villano: ', villanosOrd[villanoNum][0], 'Vida: ', villanosOrd[villanoNum][1]
				villanosOrd[villanoNum][1] -= 1
				if villanosOrd[villanoNum][1] <= 0:
					gananciasTotales += villanosOrd[villanoNum][2]
					villanoNum += 1
					if villanoNum >= len(villanosOrd):
						break
			else:
				villanoNum += 1
				if villanoNum >= len(villanosOrd):
					break
		if villanoNum >= len(villanosOrd):
			break
	print 'Horas totales trabajadas: ', horasTotales
	print 'Ganancias totales: ', gananciasTotales

if __name__ == '__main__':
	main()