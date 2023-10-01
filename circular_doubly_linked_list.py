#Lista circular doble
#Por Jorge Tomas Araujo Gonzalez 
class Nodo: 
    def __init__(self,valor):
        self.valor=valor    #Valor del nodo que agreguemos 
        self.apuntador_sig=None #Indica cuál es el nodo siguiente del actual
        self.apuntador_ant=None #Indica cuál es el nodo anterior del actual
    
class Lista:
    def __init__(self):
        self.elemento_inicial=None  #Indica cuál es el primer elemento de la lista
        self.tamaño=0               #tamaño de la lista
        self.elemento_final=None    #Indica cuál es el último elemento de la lista

    def agregar_inicio(self,valor): #Función que agrega un nodo al inicio de la lista
        nuevo_nodo=Nodo(valor)
        if self.tamaño==0:  #Si no hay ningún elemento en la lista, el elemento final e inicial = al único y nuevo 
            self.elemento_final=self.elemento_inicial=nuevo_nodo    #nodo que se encuentra en la lista y los apuntadores se mantienen en nulo
        else:       #Si la lista ya contiene al menos un elemento: 
            self.elemento_inicial.apuntador_ant=nuevo_nodo #En esta parte no creo necesario explicar paso por paso
            nuevo_nodo.apuntador_sig=self.elemento_inicial  #ya que los nombres que utilicé hacen que se pueda identificar 
            nuevo_nodo.apuntador_ant=self.elemento_final    #fácilmente lo que pasa con las variables
            self.elemento_inicial=nuevo_nodo
            self.elemento_final.apuntador_sig=self.elemento_inicial
        self.tamaño+=1 #Se aumenta el tamaño de la lista en 1
    
    def agregar_final(self,valor):  #Función que agrega un nodo al final de la lista
        nuevo_nodo=Nodo(valor)
        if self.tamaño==0:
            self.elemento_final=self.elemento_inicial=nuevo_nodo
        else:
            self.elemento_inicial.apuntador_ant=nuevo_nodo  #Lo que cambia en esta función de la anterior, es que
            nuevo_nodo.apuntador_sig=self.elemento_inicial  #el apuntador siguiente del elemento final apunta hacia el nuevo 
            nuevo_nodo.apuntador_ant=self.elemento_final    #nodo, y después el elemento final toma el valor del nuevo nodo
            self.elemento_final.apuntador_sig=nuevo_nodo
            self.elemento_final=nuevo_nodo
        self.tamaño+=1  #Se aumenta el tamaño de la lista en 1

    def borrado_inicio(self):   #Función que extrae un nodo al inicio de la lista
        if self.tamaño==0:  #Si no hay nada en la lista se imprime:
            print('lista vacía')    #ya que no se puede extraer nada
            return
        elif self.tamaño==1:    #Si la lista solo tiene 1 elemento:
            self.elemento_final=self.elemento_inicial=None  #los elementos final e inicial son nulos
        else:   #Si la lista tiene más de 1 elemento:
            self.elemento_inicial=self.elemento_inicial.apuntador_sig   
            self.elemento_final.apuntador_sig=self.elemento_inicial
            self.elemento_inicial.apuntador_ant=self.elemento_final
        self.tamaño-=1  #Se decrementa en 1 el tamaño de la lista
            
    def borrado_final(self):    #Función que extrae un nodo al final de la lista
        if self.tamaño==0:  #Si no hay nada en la lista se imprime:
            print('lista vacía')    #ya que no se puede extraer nada
            return
        elif self.tamaño==1:    #Si la lista solo tiene 1 elemento:
            self.elemento_final=self.elemento_inicial=None  #los elementos final e inicial son nulos
        else:
            self.elemento_final=self.elemento_final.apuntador_ant
            self.elemento_final.apuntador_sig=self.elemento_inicial
            self.elemento_inicial.apuntador_ant=self.elemento_final
        self.tamaño-=1  #Se decrementa en 1 el tamaño de la lista

def imprimir_nodo():  #Esta función imprime cada nodo de la lista con sus respectivos apuntadores
    print('\n')
    for i in range (0,lista.tamaño):
        print(lista.elemento_inicial.apuntador_ant.valor,   #Se imprime el apuntador anterior
        '--',lista.elemento_inicial.valor,                  #Se imprime el nodo actual
        '--',lista.elemento_inicial.apuntador_sig.valor)    #Se imprime el apuntador siguiente
        lista.elemento_inicial=lista.elemento_inicial.apuntador_sig     #El elemento inicial toma el valor
    print('\n')                                                         #de su apuntador siguiente para poder
                                                                        #recorrer la lista 
def imprimir_lista():   #Esta función la hice para imprimir toda la
    lista_corrido=[]    #lista en un solo renglon
    for k in range(0,lista.tamaño):
        lista_corrido.append(lista.elemento_inicial.valor)
        lista.elemento_inicial=lista.elemento_inicial.apuntador_sig
    print('\nLista caputrada:\n',lista_corrido)

lista=Lista()
lista.agregar_inicio(9)
lista.agregar_inicio(2)
lista.agregar_inicio(3)
lista.agregar_inicio(7)
lista.agregar_inicio(10)
lista.agregar_final(5)
lista.agregar_final(1)
lista.agregar_final(8)
lista.agregar_final(6)
lista.agregar_final(4)
imprimir_lista()
#Lista 10,7,3,2,9,5,1,8,6,4
lista.borrado_inicio()
lista.borrado_inicio()
lista.borrado_final()
imprimir_lista()
imprimir_nodo()
#Por Jorge Tomás Araujo González, 2/10/2021
