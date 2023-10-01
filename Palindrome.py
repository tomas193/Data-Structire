#Programa para determinar si una palabra u oración es palíndromo
#Programa elaborado por Jorge Tomás Araujo González     7/9/2021
import math
class pila: #Clase pila, dentro de la cual irán todos los métodos que requiere una pila de datos
    def __init__(self,tamaño): #funcion donde se declaran los atributos de la clase
        self.tamaño=tamaño
        self.lista=[]

    def vacia(self): #Funcion que nos permite saber si la pila está vacía; si es así,
        if self.top==-1:    #nada se ejecutará
            return True
        else:
            return False

    def insertar(self, item):   #Funcion donde se agregan nuevos elementos a la lista, la cual
        self.lista.append(item) #no tiene un límite determinado ya que el usuario puede escribir un palindromo 
                                #tan largo como desee
oración=input("\nIngrese una palabra u oración: ")
y=len(oración)  
x=pila(y)   #'x' es un objeto donde se guardan las letras sin espacios
bandera=0   #variable que indicará si lo que ingresó el usuario es palabra u oración

for i in range(0,y):    #ciclo for donde se irá agregando cada letra a 'x'
    if oración[i]!=" ": #si el elemento de oración en la posición i es diferente de un espacio,   
        x.insertar(oración[i])  #entonces agrega el elemnto
    else:
        bandera+=1  #si no, bandera aumenta cada vez que hay un espacio
y=len(x.lista)  #se mide la longitud de la pila sin espacios
z=math.ceil(y/2)    #se encuentra la mitad de la pila para comparar ambas mitades
for j in range (0,z):   #comparación de ambas mitades
    if x.lista[j].upper()==x.lista[y-1].upper():    #Si las letras del inicio y fin son iguales,
        y-=1        
        print(x.lista[j], x.lista[y])            #entonces sigue la comparación. Si no, se interrumpe
    else:                                        #el ciclo y se determina que no es un palíndromo.
        if bandera>0:                               
            print(f'La oración "{oración}" no es un palíndromo\n')  #De la línea 33 a 42, imprime si 
        else:                                                       #la oración es un palíndromo o no
            print(f'La palabra "{oración}" no es un palíndromo\n')  #y dependiendo si bandera es mayor a 1,
        break                                                       #se imprime que lo ingresado por el usuario
    if j==z-1:                                                      #es una palabra u oración.
        if bandera>0:
            print(f'La oración "{oración}" es un palíndromo\n')
        else:
            print(f'La palabra "{oración}" es un palíndromo\n')

        


