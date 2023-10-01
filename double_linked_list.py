#Por Jorge Tomas Araujo Gonzalez
class Nodo: 
    def __init__(self,valor):
        self.valor=valor
        self.apuntador_sig=None
        self.apuntador_ant=None
    
class Lista:
    def __init__(self):
        self.elemento_inicial=None
        self.tamaño=0
        self.elemento_final=None
    
    def vacio(self):
        if self.tamaño==0:
            return True
        else:
            return False

    def agregar_inicio(self,valor):
        nuevo_nodo=Nodo(valor)
        if self.tamaño==0:
            self.elemento_final=self.elemento_inicial=nuevo_nodo
        else:
            aux=self.elemento_inicial
            nuevo_nodo.apuntador_sig=self.elemento_inicial
            aux.apuntador_ant=nuevo_nodo
            self.elemento_inicial=nuevo_nodo
            print(self.elemento_inicial.valor, self.elemento_inicial.apuntador_sig.valor)
        self.tamaño+=1
    
    def agregar_final(self,valor):
        nuevo_nodo=Nodo(valor)
        if self.tamaño==0:
            self.elemento_final=self.elemento_inicial=nuevo_nodo
        else:
            nuevo_nodo.apuntador_ant=self.elemento_final
            self.elemento_final.apuntador_sig=nuevo_nodo
            self.elemento_final=nuevo_nodo
        self.tamaño+=1

    def extraer_inicio(self):
        if self.tamaño==0:
            print('\nLista vacía')
        else:
            if self.tamaño==1:
                self.elemento_inicial=self.elemento_final=None   
                self.tamaño-=1   
            else:
                self.elemento_inicial=self.elemento_inicial.apuntador_sig
                self.elemento_inicial.apuntador_ant=None
                self.tamaño-=1

    def extraer_final(self):
        if self.tamaño==0:
            print('\nLista vacía')
        else:
            if self.tamaño==1:
                self.elemento_inicial=self.elemento_final=None   
                self.tamaño-=1   
            else:
                self.elemento_final=self.elemento_final.apuntador_ant
                self.elemento_final.apuntador_sig=None
                self.tamaño-=1


lista=Lista()
lista.agregar_inicio(21)
lista.agregar_inicio(5)
lista.agregar_inicio(3)
lista.agregar_final(9)
print(lista.elemento_inicial.valor, lista.elemento_final.valor)
print('tamaño: ',lista.tamaño)
lista.extraer_inicio()
print(lista.elemento_inicial.valor, lista.elemento_final.valor)
print('tamaño: ',lista.tamaño)
lista.extraer_final()
print(lista.elemento_inicial.valor, lista.elemento_final.valor)
print('tamaño: ',lista.tamaño)
#Lista: 3, 5, 21, 9


