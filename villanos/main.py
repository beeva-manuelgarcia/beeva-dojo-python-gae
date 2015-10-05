__author__ = 'manuel'
from random import randint

DIAS=int(7)
HORAS=int(24)
VILLANOMAX=int(3)

def generarVillanos():
	#Nombre, vida, recompensa, distancia, villano(1),
	v1=['A', randint(1,30), randint(1000,3000),randint(1,10),randint(0,1)]
	v2=['B', randint(1,30), randint(1000,3000),randint(1,10),randint(0,1)]
	v3=['C', randint(1,30), randint(1000,3000),randint(1,10),randint(0,1)]

	matriz=[v1,v2,v3]
	return matriz

def ordenarVillanos(villanos):
	villanosOrd=villanos
	villanosOrd.sort(lambda x,y: cmp(x[3],y[3]))
	return villanosOrd


villanos=generarVillanos()
print 'Matriz M = ',villanos

#ordenamos villanos por distancia para ir a por ellos
print ordenarVillanos(villanos)

aux=ordenarVillanos(villanos)
villano=0
vida=1
horatotales=0
for i in range(DIAS):
    print 'Dia: ',int(i+1)
    for j in range(HORAS):
		print 'Hora: ', j, 'Villano: ', aux[villano][0], 'Vida: ', aux[villano][1]
		aux[villano][1]=aux[villano][1]-1
		if aux[villano][1]<=0:
			villano += 1
			if villano>=VILLANOMAX:
				break
    if villano>=VILLANOMAX:
        break




