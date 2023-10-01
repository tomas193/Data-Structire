#Jorge Tomás Araujo González 24/8/2021
from math import trunc
from random import randint, random, randrange #Ordenamiento por inserción

límite=8
lista=[15,67,8,16,44,27,12,35] #Lista donde se guardarán los números a organizar

#Ciclo for que se repetirá desde 0 hasta el número límite que ingresó el usuario
#Dentro de este ciclo, la variable x toma un valor aleatorio y se guarda en la lista 
'''for j in range(0,límite):
    x=randint(1,100) #Variable de número aleatorio que irá dentro de la lista
    lista.append(x)'''
print (f'\nLista desordenada: {lista}\n')

#Aca hay un ciclo for, que va desde 1 hasta la cantidad de números que el usuario quiere ordenar
#Dentro del for hay un while, si se cumple la condición de que a sea mayor o igual a 0 y el número en 
#la posición 'a' sea mayor que la variable aux, entonces la posición "a+1" toma el valor que estaba en 
#la posición 'a'. Después de este intercambio, el número guardado en aux se guarda en la posición 'a+1' de
#la lista.
for i in range (1,len(lista)):
    aux=lista[i]
    a=i-1
    while a>=0 and lista[a]>aux:
        lista[a+1]=lista[a]
        a=a-1
    lista[a+1]=aux
    if i+1<límite:
        print(f'Corrida {i} {lista}')
    else:
        print(f'Corrida final {lista}')
