class Node: #Se declaran todos los atributos del nodo
    def __init__(self,valor):
        self.valor=valor
        self.padre=None
        self.es_raiz=False
        self.derecho=None
        self.izquierdo=None
        self.es_derecho=False
        self.es_izquierdo=False

class tree:    #Se declaran los atributos del árbol y se agregan los métodos necesarios
    def __init__(self):
        self.root=None  #Iniciamos la raíz en none
        self.size=0   #Peso inicial es 0

    def node_insertion(self,valor): #Add new node in the tree
        new_node=Node(valor)
        if self.size==0:  #If Size=0, new node = root
            new_node.es_raiz=True
            self.root=new_node
        else:   #Si ya hay una raíz, entonces se llama a la función get_posicion para
            nodo_padre,lado=self.get_posicion(valor)    #obtener la posición del nodo
            if lado=='derecho':
                nodo_padre.derecho=new_node
                new_node.es_derecho=True
            else:
                nodo_padre.izquierdo=new_node
                new_node.es_izquierdo=True
            new_node.padre=nodo_padre
        self.size+=1
        print('\nAdded Node: ',new_node.valor)
        print('Tree Size: ',self.size)
        print('Root: ',self.root.valor)
        print('In Order: ',self.in_order(tree.root))

    def get_posicion(self,valor):   #Función que determina la posición del nodo
        aux=self.root
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

    def buscar(self,valor,nodo):    #Función para buscar un nodo en el arbol
        if nodo == None:   #Si la raíz=None, no hay nada que buscar 
            return None
        else:
            if valor == nodo.valor:     #Si el valor buscado = a algun nodo en el árbol,  
                    #se imprime nodo encontrado, si no se vuelve a llamar la función
                print("NODE FOUND")
                return nodo
            elif valor <= nodo.valor:
                return self.buscar(valor,nodo.izquierdo)
            else:
                return self.buscar(valor,nodo.derecho)

    def eliminar_nodo(self,valor):  #Método para eliminar algún nodo
        if self.root==None:
            return
        nodo_a_eliminar=self.buscar(valor,self.root)
        if nodo_a_eliminar==None:
            return
        nodo_hijo=self.num_hijos(nodo_a_eliminar)
        
        if nodo_hijo==0:    #Si el nodo a eliminar no tiene ningún hijo:
            if nodo_a_eliminar.es_raiz==True:#Si el nodo a eliminar es la raíz:
                self.root=None
            else:#Si no es raíz, entonces:
                if nodo_a_eliminar.es_derecho==True:
                    nodo_a_eliminar.padre.derecho=None
                else:
                    nodo_a_eliminar.padre.izquierdo=None
                nodo_a_eliminar.padre=None

        elif nodo_hijo==1:  #Si el nodo a eliminar tiene un hijo:
            if nodo_a_eliminar.es_raiz==True:   #Si el nodo a eliminar es la raíz:
                self.root=self.root.izquierdo or self.root.derecho
                self.root.padre.izquierdo=None
                self.root.padre.derecho=None
                self.root.padre=None
                self.root.es_derecho=None
                self.root.es_izquierdo=None
                self.root.es_raiz=True
            else:   #Si no es raíz, entonces:
                if nodo_a_eliminar.es_izquierdo==True:
                    if nodo_a_eliminar.izquierdo!=None:
                        nodo_a_eliminar.padre.izquierdo=nodo_a_eliminar.izquierdo
                    else:
                        nodo_a_eliminar.padre.izquierdo=nodo_a_eliminar.derecho
                else:
                    if nodo_a_eliminar.izquierdo!=None:
                        nodo_a_eliminar.padre.derecho=nodo_a_eliminar.izquierdo
                        nodo_a_eliminar.izquierdo.padre=nodo_a_eliminar.padre
                        nodo_a_eliminar.izquierdo.es_izquierdo=False
                        nodo_a_eliminar.izquierdo.es_derecho=True
                    else:
                        nodo_a_eliminar.padre.derecho=nodo_a_eliminar.derecho
                        nodo_a_eliminar.derecho.padre=nodo_a_eliminar.padre
                    nodo_a_eliminar.padre=None
                        
        elif nodo_hijo==2:  #Si el nodo a eliminar tiene 2 hijos:
            if nodo_a_eliminar.es_raiz==True:   #Si el nodo a eliminar es la raíz:
                nueva_raiz=self.sucesor(self.root)
                self.root.derecho.padre=nueva_raiz[1]
                if nueva_raiz[0]!=nueva_raiz[1]:
                    if nueva_raiz[1].izquierdo!=None: #si el sucesor tiene hijos
                        nueva_raiz[0].derecho=nueva_raiz[1].izquierdo
                        nueva_raiz[1].izquierdo.padre=nueva_raiz[1].padre
                        nueva_raiz[0].padre=nueva_raiz[1]
                        nueva_raiz[1].izquierdo=nueva_raiz[0]
                    else: #si el sucesor no tiene hijos
                        nueva_raiz[1].izquierdo=nueva_raiz[0]
                        nueva_raiz[0].padre=nueva_raiz[1]
                        if nueva_raiz[1].padre!=nueva_raiz[0]:
                            nueva_raiz[1].padre.derecho=None
                        else:
                            nueva_raiz[0].derecho=None
                        
                nueva_raiz[1].derecho=self.root.derecho
                self.root.es_raiz=False
                self.root.izquierdo=None
                self.root.derecho=None
                self.root=nueva_raiz[1]
                self.root.es_derecho=None
                self.root.es_izquierdo=None
                self.root.es_raiz=True
                self.root.padre=None

            else:   #Si no es raíz, entonces:
                nuevo_nodo=nodo_a_eliminar.izquierdo
                nuevo_nodo.padre=nodo_a_eliminar.padre
                nodo_a_eliminar.derecho.padre=nuevo_nodo
                nuevo_nodo.derecho=nodo_a_eliminar.derecho
                
                if nodo_a_eliminar.es_izquierdo==True:
                    nodo_a_eliminar.padre.izquierdo=nodo_a_eliminar.izquierdo
                else:
                    nodo_a_eliminar.padre.derecho=nodo_a_eliminar.izquierdo
                    nuevo_nodo.es_izquierdo=False
                    nuevo_nodo.es_derecho=True

                nodo_a_eliminar.izquierdo=None
                nodo_a_eliminar.derecho=None
                nodo_a_eliminar.es_derecho=None
                nodo_a_eliminar.es_izquierdo=None
                nodo_a_eliminar.padre=None

        self.size-=1
        print('\nRemoved Node: ',nodo_a_eliminar.valor)
        print('Tree Size: ',self.size)
        if self.size>0:
            print('Root: ',self.root.valor)
            print('In Order: ',tree.in_order(tree.root))
        else:
            print('Root: ',self.root)            
        
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
            
tree=tree() #object tree

#valores=[67,44,22,9,37,39,50,47,85,73,90,88,94]
#for i in valores:
#    tree.node_insertion(i)

def uno():
    var=input(" ")
    if var=="x":
        return
    else:
        tree.node_insertion(int(var))
    uno()

def dos():
    var=input(" ")
    if var=="x":
        return
    else:
        tree.eliminar_nodo(int(var))
    dos()

def tres():
    var=input(" ")
    if var=="x":
        return
    else:
        print(tree.buscar(int(var),tree.root))
    tres()

while True:
    print("\nSelect an Option")
    print("1-Insert Node  2-Delete Node  3-Search Node  4-End Program")
    x=input(" ")
    if int(x)==4:
        break
    elif int(x)==1:
        uno()
    elif int(x)==2:
        dos()
    elif int(x)==3:
        tres()
    else:
        print("Enter a valid option")

#Por Jorge Tomás Araujo González   revisited version  2023
