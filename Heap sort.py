#Jorge Tomás Araujo González 2/9/2021
def heapsort(a): #Función principal, donde se mandan llamar las otras funciones y tiene como parámetro la lista
    heapify(a,len(a)) #Se manda llamar la función heapify con parámetros 'a' y 'len(a)'
    end=len(a)-1 #Esta variable indica el tope de nuestra lista
    while end>0: #Mientras end sea mayor que 0 se ejecuta lo siguiente:
        a[end], a[0]=a[0],a[end] #Se intercambia el último valor de la lista con el primero
        end-=1 #Se decrementa la variable end
        sift_down(a,0,end)  #Se manda llamar la función sift_down con parámetros a,0,end

def heapify(a,count):
    start=int((count-2)/2) #Variable que nos sirve para iniciar el ordenamiento a partir del padre de los últimos hijos en toda la lista
    print('posición inicial', start) #Se imprime la posición en la que inicia start
    while start>=0: #Mientras start sea mayor o igual que 0, se ejecuta lo siguiente:
        sift_down(a,start,count-1) #Se manda llamar la función sift_down con sus respectivos parámetros
        start-=1    #Se decrementa start para que se haga la comparación entre otro padre e hijo 
    
def sift_down(a,start,end):
    root=start
    while (root*2+1)<=end:  #Mientras (root*2)+1 sea menor o igual que el tamaño de la lista, se ejecutará lo siguiente:
        child=root*2+1  #la posición child se calcula: (root*2)+1, que es la distancia a la que se encuentra del padre
        swap=root
        if a[swap]<a[child]:
            swap=child
        if (child+1)<=end and a[swap]<a[child+1]: #Si la posición hijo+1 es menor o igual a end, y el valor en swap es menor al de la posición hijo+1:
            swap=child+1    
        if swap != root:    #Si 'swap' es diferente de 'root' entonces:
            a[root],a[swap],=a[swap],a[root]    #El valor en la posición root y swap intercambian lugar
            root=swap
        else:   #Si ninguna de esas condiciones se cumple, regresamos a la función heapsort
            return
        
a=[13,6,45,10,3,22,90,4,74,61]
heapsort(a)
print(a)