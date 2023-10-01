#Árbol binario
#Por Jorge Tomás Araujo González    10/24/2021
class Nodo: #Se declaran todos los atributos del nodo
    def __init__(self,valor):
        self.valor=valor
        self.padre=None
        self.es_raiz=False
        self.derecho=None
        self.izquierdo=None
        self.es_derecho=False
        self.es_izquierdo=False
        self.height=1
class arbol:    #Se declaran los atributos del árbol y se agregan los métodos necesarios
    def __init__(self):
        self.raiz=None  #Iniciamos la raíz en none
        self.tamaño=0   #Peso inicial es 0

    def nuevo_nodo(self,valor): #Método para agregar un nuevo nodo en el árbol
        nodo_nuevo=Nodo(valor)
        if self.tamaño==0:  #Si no hay nada en el árbol, el nuevo nodo se convierte en la raíz
            nodo_nuevo.es_raiz=True
            self.raiz=nodo_nuevo
        else:   #Si ya hay una raíz, entonces se llama a la función get_posicion para
            nodo_padre,lado=self.get_posicion(valor)    #obtener la posición del nodo
            if lado=='derecho':
                nodo_padre.derecho=nodo_nuevo
                nodo_nuevo.es_derecho=True
            else:
                nodo_padre.izquierdo=nodo_nuevo
                nodo_nuevo.es_izquierdo=True
            nodo_nuevo.padre=nodo_padre
        self.inspect_insercion(nodo_nuevo)
        self.tamaño+=1
        print('\nnodo añadido: ',nodo_nuevo.valor)
        print('raíz: ',self.raiz.valor)
        print('tamaño: ',self.tamaño)
        print('in order: ',self.in_order(arbol.raiz))

    def get_posicion(self,valor):   #Función que determina la posición del nodo
        aux=self.raiz
        while aux:  #Mientras aux tenga un valor:
            prev=aux
            if prev.valor<=valor:   #Si el valor previo es menor o igual al nodo:
                aux=aux.derecho     #se le asigna el lado derecho al nodo
                lado='derecho'
            else:                   #De lo contrario, se le asigna el lado izquierdo 
                aux=aux.izquierdo
                lado='izquierdo'
        return (prev,lado)

    def in_order(self,nodo):    #Función que acomoda el árbol en la forma izq.-nodo-der.
        if nodo:
            self.in_order(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self.in_order(nodo.derecho)
        return

    def post_order(self, nodo): #Función que acomoda el árbol en la forma izq.-der.-nodo
        if nodo:
            self.post_order(nodo.izquierdo)
            self.post_order(nodo.derecho)
            print(nodo.valor, end='  ')

    def pre_order(self,nodo):   #Función que acomoda el árbol en la forma nodo-izq.-der.
        if nodo:
            print(nodo.valor, end='   ')
            self.pre_order(nodo.izquierdo)
            self.pre_order(nodo.derecho)

    def buscar(self,valor,nodo):    #Función para buscar un nodo
        if nodo == None:   #Si la raíz=None, no hay nada que buscar 
            print("Nodo no encontrado")
        else:
            if valor == nodo.valor:     #Si el valor buscado = a algun nodo en el árbol,  
                    #se imprime nodo encontrado, si no se vuelve a llamar la función
                return nodo
            elif valor <= nodo.valor:
                return self.buscar(valor,nodo.izquierdo)
            else:
                return self.buscar(valor,nodo.derecho)

    def eliminar_nodo(self,valor):  #Método para eliminar algún nodo
        nodo_a_eliminar=self.buscar(valor,self.raiz)
        nodo_hijo=self.num_hijos(nodo_a_eliminar)
        if nodo_hijo==0:    #Si el nodo a eliminar no tiene ningún hijo:
            if nodo_a_eliminar.es_raiz==True:#Si el nodo a eliminar es la raíz:
                self.raiz=None
            else:#Si no es raíz, entonces:
                if nodo_a_eliminar.es_derecho==True:
                    nodo_a_eliminar.padre.derecho=None
                else:
                    nodo_a_eliminar.padre.izquierdo=None
        elif nodo_hijo==1:  #Si el nodo a eliminar tiene un hijo:
            if nodo_a_eliminar.es_raiz==True:   #Si el nodo a eliminar es la raíz:
                self.raiz=self.raiz.izquierdo or self.raiz.derecho
                self.raiz.padre=None
                self.raiz.es_derecho=None
                self.raiz.es_izquierdo=None
                self.raiz.es_raiz=True
            else:   #Si no es raíz, entonces:
                if nodo_a_eliminar.es_izquierdo==True:
                    if nodo_a_eliminar.izquierdo!=None:
                        nodo_a_eliminar.padre.izquierdo=nodo_a_eliminar.izquierdo
                    else:
                        nodo_a_eliminar.padre.izquierdo=nodo_a_eliminar.derecho
                else:
                    if nodo_a_eliminar.izquierdo!=None:
                        nodo_a_eliminar.padre.derecho=nodo_a_eliminar.izquierdo
                    else:
                        nodo_a_eliminar.padre.derecho=nodo_a_eliminar.derecho
                        
        elif nodo_hijo==2:  #Si el nodo a eliminar tiene 2 hijos:
            if nodo_a_eliminar.es_raiz==True:   #Si el nodo a eliminar es la raíz:
                nueva_raiz=self.sucesor(self.raiz)
                if nueva_raiz[0].derecho==None:
                    nueva_raiz[1].padre=None
                    self.raiz.derecho.padre=nueva_raiz[1]
                    nueva_raiz[1].derecho=self.raiz.derecho
                    nueva_raiz[1].izquierdo=None
                    self.raiz=nueva_raiz[1]
                    self.raiz.es_derecho=None
                    self.raiz.es_izquierdo=None
                    self.raiz.es_raiz=True
                else:
                    nueva_raiz[1].padre.derecho=None
                    nueva_raiz[1].padre=None
                    self.raiz.izquierdo.padre=nueva_raiz[1]
                    self.raiz.derecho.padre=nueva_raiz[1]
                    nueva_raiz[1].derecho=self.raiz.derecho
                    nueva_raiz[1].izquierdo=self.raiz.izquierdo
                    self.raiz=nueva_raiz[1]
                    self.raiz.es_derecho=None
                    self.raiz.es_izquierdo=None
                    self.raiz.es_raiz=True
            else:   #Si no es raíz, entonces:
                if nodo_a_eliminar.es_izquierdo==True:
                    nodo_a_eliminar.padre.izquierdo=nodo_a_eliminar.izquierdo
                    nuevo_nodo=nodo_a_eliminar.izquierdo
                    nuevo_nodo.padre=nodo_a_eliminar.padre
                    nodo_a_eliminar.derecho.padre=nuevo_nodo
                    nuevo_nodo.derecho=nodo_a_eliminar.derecho
                else:
                    nodo_a_eliminar.padre.derecho=nodo_a_eliminar.izquierdo
                    nuevo_nodo=nodo_a_eliminar.izquierdo
                    nuevo_nodo.padre=nodo_a_eliminar.padre
                    nodo_a_eliminar.derecho.padre=nuevo_nodo
                    nuevo_nodo.derecho=nodo_a_eliminar.derecho
                    nuevo_nodo.es_izquierdo=False
                    nuevo_nodo.es_derecho=True
        self._inspect_deletion(nodo_a_eliminar)
        self.tamaño-=1
        print('\nnodo eliminado: ',nodo_a_eliminar.valor)
        print('tamaño: ',self.tamaño)
        print('raíz: ',self.raiz.valor)
        print('in order: ',arbol.in_order(arbol.raiz))
        
    def sucesor(self,nodo): #Método para encontrar el nodo mas
        itr=nodo.izquierdo  #a la derecha de la rama izquierda
        if itr.derecho==None:   
            itr_2=itr
        else:
            itr_2=itr.derecho
            while itr_2:
                if itr_2.derecho==None:
                    break
                else:
                    itr_2=itr_2.derecho
        return itr,itr_2

    def num_hijos(self,nodo):   #Método para determinar el número de hijos
        cont=0                  #que tiene un nodo
        if nodo.derecho:
            cont+=1
        if nodo.izquierdo:
            cont+=1
        return cont
    
    def get_height(self,nodo):  #Método para conseguir la altura del nodo
        if nodo==None:return 0
        return nodo.height

    def taller_child(self,nodo):    #Método para conseguir el hijo mayor
        izquierdo=self.get_height(nodo.izquierdo)
        derecho=self.get_height(nodo.derecho)
        return nodo.izquierdo if izquierdo>=derecho else nodo.derecho

    def rotacion_derecha(self,z):   #Método para hacer una rotación a la derecha
        sub_raiz = z.padre
        y=z.izquierdo
        t3=y.derecho
        y.derecho=z
        z.padre=y
        z.izquierdo=t3
        z.es_izquierdo=False    #cambiando las banderas de z
        z.es_derecho=True
        #t3.es_izquierdo=True
        #t3.es_derecho=False
        if t3!=None: t3.padre=z
        y.padre=sub_raiz
        if y.padre==None:
            self.raiz=y
            y.es_raiz=True
            z.es_raiz=False
        else:
            if y.padre.izquierdo==z:
                y.padre.izquierdo=y
                y.es_izquierdo=True
                y.es_derecho=False
            else:
                y.padre.derecho=y
                y.es_izquierdo=False
                y.es_derecho=True
        z.height=1+max(self.get_height(z.izquierdo),
        self.get_height(z.derecho))
        y.height=1+max(self.get_height(y.izquierdo),
        self.get_height(y.derecho))

    def rotacion_izquierda(self,z): #Método para hacer una rotación a la izquierda
        sub_raiz=z.padre
        y=z.derecho
        t2=y.izquierdo
        y.izquierdo=z
        z.padre=y
        z.derecho=t2
        z.es_izquierdo=True #cambiando las banderas de z
        z.es_derecho=False
        #t2.es_izquierdo=False
        #t2.es_derecho=True
        if t2!=None: t2.padre=z
        y.padre=sub_raiz
        if y.padre ==None:
            self.raiz=y
            y.es_raiz=True  #cambiando las banderas de si es raiz o no
            z.es_raiz=False
        else:
            if y.padre.izquierdo==z:
                y.padre.izquierdo=y
                y.es_izquierdo=True
                y.es_derecho=False
            else:
                y.padre.derecho=y
                y.es_izquierdo=False
                y.es_derecho=True
        z.height=1+max(self.get_height(z.izquierdo),
        self.get_height(z.derecho))
        y.height=1+max(self.get_height(y.izquierdo),
        self.get_height(y.derecho))

    def inspect_insercion(self,nodo,path=[]):   #Método que checa el balance del árbol al momento de agregar un nodo
        if nodo.padre==None:return
        path=[nodo]+path
        izquierdo_height=self.get_height(nodo.padre.izquierdo)
        derecho_height=self.get_height(nodo.padre.derecho)
        print('altura izq y der: ',izquierdo_height,derecho_height)
        if abs(izquierdo_height - derecho_height)>1:
            nodo.padre.es_raiz=False
            path=[nodo.padre]+path
            self.balancear_nodo(path[0],path[1],path[2])
            self.raiz.es_raiz=True
            return
        new_height=1+nodo.height
        if new_height>nodo.padre.height:
            nodo.padre.height=new_height
        self.inspect_insercion(nodo.padre,path)

    def balancear_nodo(self,z,y,x): #Método que balancea el arbol cambiando de lugar los nodos
        if y==z.izquierdo and x==y.izquierdo:   #cuando manda llamar a la rotación izq. o der.
            self.rotacion_derecha(z)
        elif y==z.izquierdo and x==y.derecho:
            self.rotacion_izquierda(y)
            self.rotacion_derecha(z)
        elif y==z.derecho and x==y.derecho:
            self.rotacion_izquierda(z)
        elif y==z.derecho and x==y.izquierdo:
            self.rotacion_derecha(y)
            self.rotacion_izquierda(z)
        else:
            raise Exception('z,y,x configuracion del nodo no reconocida')

    def _inspect_deletion(self,nodo):   #Método que checa el balance del arbol cuando se elimina un nodo
        if nodo==None:return
        left_height = self.get_height(nodo.izquierdo)
        right_height= self.get_height(nodo.derecho)
        if abs(left_height-right_height)>1:
            y=self.taller_child(nodo)
            x=self.taller_child(y)
            self.balancear_nodo(nodo,y,x)
        self._inspect_deletion(nodo.padre)

arbol=arbol()
valores=[18,17,16,6,9,21,43,20,42,41,3]
for i in valores:
    arbol.nuevo_nodo(i)

'''arbol.eliminar_nodo(43) #Eliminando todos los nodos 
arbol.eliminar_nodo(18)
arbol.eliminar_nodo(16)
arbol.eliminar_nodo(21)
arbol.eliminar_nodo(9)
arbol.eliminar_nodo(6)
arbol.nuevo_nodo(5) #Agregando nuevos nodos
arbol.nuevo_nodo(4)'''

