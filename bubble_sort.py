#Jorge Tomás Araujo González 3/17/2021
lista=[25,60,45,35,12,92,85,30]

print (f'\nLista desordenada\n{lista}')

for i in range(0,len(lista)):
    for k in range(0,len(lista)-1):
        if lista[k]>lista[k+1]:
            aux=lista[k]
            lista[k]=lista[k+1]
            lista[k+1]=aux

print(f'\nLista ordenada\n{lista}')
        

