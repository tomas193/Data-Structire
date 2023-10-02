#Jorge Tomás Araujo González 26/8/2021
#Ordenamiento rapido (quicksort)
from math import trunc
from random import randint
while True:
    límite=int(input('\nIngrese la cantidad de números a ordenar: ')) #Ciclo while donde se introduce la variable que sea 
    if límite>=1 and límite<=50:                                    #mayor o igual a 1, y menor o igual a 100.
        break

lista=[] #Lista donde se guardarán los números a organizar

#Ciclo for que se repetirá desde 0 hasta el número límite que ingresó el usuario
#Dentro de este ciclo, la variable x toma un valor aleatorio y se guarda en la lista 
for j in range(0,límite):
    x=randint(1,100) #Variable de número aleatorio que irá dentro de la lista
    lista.append(x)
print (f'\nLista desordenada:\n{lista}\n')

#Dentro de esta función llamada partición, se declaran dos listas nuevas. Una para los números mayores al pivote
#y otra para los números menores al pivote. Esta comparación se hace mediante un ciclo for que empieza en 1 -ya que
#nuestro pivote está en la posición 0-, y termina en el número de valores que tenga la lista.
def particion(lista):
    lista_mayores=[]
    lista_menores=[]
    pivote=lista[0]
    for i in range(1,len(lista)):
        if pivote<lista[i]:
            lista_mayores.append(lista[i])
        else:
            lista_menores.append(lista[i])
    return lista_menores,pivote,lista_mayores

#Esta función llamada quicksort empieza a ordenar la lista menor, mayor, y el pivote, cuando se igualan a la función partición
#y cada vez se hacen más pequeñas hasta tener un solo elemento o ninguno. Entonces, se empiezan a comparar las listas otra vez
#y se juntan hasta llegar a la lista final.
def quicksort(lista):
    if len(lista)<2:
        return lista
    lista_menores, pivote, lista_mayores=particion(lista)
    return quicksort(lista_menores)+[pivote]+quicksort(lista_mayores)
print(f'Lista ordenada:\n{quicksort(lista)}')




