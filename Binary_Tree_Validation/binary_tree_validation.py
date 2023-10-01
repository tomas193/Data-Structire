#Program to verify if a binary tree is valid or not
#input format:		left child    root    right child
while True: #Ciclo while donde se introduce el número de nodos
    try:    #para evitar el error
        num_nodos=int(input("numero de nodos: "))  
        if 0<=num_nodos<=1000000:
            break    #si el numero esta dentro del rango se corta el ciclo
        else:                   #Si no, se imprime fuera de rango y vuelve pedir un número
            print('FUERA DE RANGO')    
    except ValueError:  #Si lo que ingresó el usuario es diferente de un número entero se imprime:
        print('INGRESE UN NÚMERO ENTERO')
        continue
valido=True
nodos=[] #lista donde se guardarán los nodos juntos con las posiciones de sus hijos
for i in range(0,num_nodos):    #Ciclo donde se agregan los nodos a la lista y se verifica que no haya errores
    nodo=input().split()    #La entrada de string se convierte en una lista sin espacios 
    while len(nodo)<=2 or int(nodo[1])>num_nodos-1 or int(nodo[2])>num_nodos-1:
        print('Ingrese un valor válido')    #En este ciclo se evita que un nodo tenga un hijo en 
        nodo=input().split()        #una posición no válida
    while nodo[1]==nodo[2]:
        if i==0:        
            print('Ingrese una raíz válida')    #Si la raíz no tiene hijos, entonces no es un 
            nodo=input().split()                #árbol válido
        elif int(nodo[1])!=-1 and int(nodo[2])!=-1: #Si el nodo introducido tiene hijos con posición distinto a -1
            print('Ingrese un valor válido')        #pero ambos de igual valor, entonces no es un nodo válido
            nodo=input().split()
        else:
            break
    nodos.append(nodo)
    if i>0 and int(nodo[1])!=-1 and int(nodo[2])!=-1:   #Para evitar que 2 nodos tengan un mismo hijo
        if nodos[i-1][2]==nodos[i][1] or nodos[i-1][1]==nodos[i][2] or nodos[i-1][1]==nodos[i][1] or nodos[i-1][2]==nodos[i][2]:
            print('ARBOL NO VALIDO')
            valido=False
            break
#Programa principal
def comprobar():    #Función que se manda llamar si la bandera valido=True y num_nodos mayor a 1
    for k in range(0,num_nodos):
        if int(nodos[k][2])>0:# lado derecho
            if int(nodos[k][0])<int(nodos[int(nodos[k][2])][0]):#Se verifica que el hijo derecho sea mayor a su padre
                if int(nodos[int(nodos[k][2])][1])>0:   #si la posición del hijo es mayor a 0:
                    if int(nodos[k][0])<int(nodos[int(nodos[int(nodos[k][2])][1])][0]):#Se compara que el nieto izquierdo sea mayor que el abuelo
                        correcto=True
                    else:
                        correcto=False
                        break
                else:
                    correcto=True
            else:
                correcto=False
                break
        if int(nodos[k][1])>0:#lado izquierdo
            if int(nodos[k][0])>int(nodos[int(nodos[k][1])][0]):#Se verifica que el hijo izquierdo sea menor a su padre
                if int(nodos[int(nodos[k][1])][2])>0:#si la posición del hijo es mayor a 0:
                    if int(nodos[k][0])>int(nodos[int(nodos[int(nodos[k][1])][2])][0]):#Se compara que el nieto derecho sea menor que el abuelo
                        correcto=True
                    else:
                        correcto=False
                        break
                else:
                    correcto=True
            else:
                correcto=False
                break
    if correcto==True:  #Si la banderra correcto=True significa que el arbol esta correcto y se imprime:
        print('CORRECT')
    else:
        print('INCORRECT')

if num_nodos>1 and valido==True:
    comprobar()
else:
    if valido==True:
        print('CORRECT')
