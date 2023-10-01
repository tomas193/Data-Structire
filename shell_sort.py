#Jorge Tomás Araujo González 31/8/2021
from math import trunc
import math
from random import randint, random, randrange #Ordenamiento shell
while True:
    límite=int(input('Ingrese la cantidad de números a ordenar: ')) #Ciclo while donde se introduce la variable que sea 
    if límite>=1 and límite<=50:                                    #mayor o igual a 1, y menor o igual a 100.
        break
    
lista=[] #Lista donde se guardarán los números a organizar

#Ciclo for que se repetirá desde 0 hasta el número límite que ingresó el usuario
#Dentro de este ciclo, la variable x toma un valor aleatorio y se guarda en la lista 
print ('Intrduzca los números a ordenar')
for j in range(0,límite):
    x=int(input(f'{j}: ')) #Variable de número aleatorio que irá dentro de la lista
    lista.append(x)#Función que va guardando en la lista el valor que introdujo el usuario
print (f'\nLista desordenada: {lista}')
#Inicio del ordenamiento
inte=límite+1 #inte es la variable que almacenará el tamaño de la lista, el cual se irá dividiendo entre 2
while inte>1:#después de cada corrida del segundo while
    inte=(inte//2)
    band=True #La variable bandera nos servirá como indicador de hasta cuando un proceso debe parar
    while band==True:
        band=False
        i=0 #La variable 'i' sirve para que el número que está en esa posición, se compare con otro
        while i+inte<=límite-1: 
            if lista[i]>lista[i+inte]: #Comparación entre el número en la posición 'i', y el número en la posición
                aux=lista[i] #'i'+'inte'
                lista[i]=lista[i+inte]  #Si el número en la variable 'i' es mayor que el número en la posición
                lista[i+inte]=aux   # 'i'+'inte', entonces se intercambian de lugar
                band=True
            i+=1

print(f'Lista ordenada: {lista}')
elemento=int(input('\nIngrese un número a buscar: '))   #pregunta para que el usuario busque un número
mitad=límite//2

def segundo_recorrido():    #Función que se lleva a cabo si en la primera mitad de la lista no se encuentra 
    for j in range(mitad,límite):   #el número buscado
        if lista[j]==elemento:
            print (f'Valor encontrado, con {j} números por detras\n')
            break
        else: 
            if j==límite-1:
                print (f'**Valor no encontrado\n')

for k in range(0,mitad):    #ciclo for en el que se hace la comparación entre el número deseado
    if lista[k]==elemento:  #y los números que se encuentran en la lista. Si el número buscado 
        print (f'Valor encontrado, con {k} números por detras\n')   #no se encuentra en esta mitad,
        break                                           #se ejecuta la función 'segundo_recorrido'
    else: 
        if k==mitad-1:
            segundo_recorrido()

