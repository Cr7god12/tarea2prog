class Cola:
    def __init__(self, n):
        self.__arreglo = [0]*(n+1)
        self.__inicio = 0
        self.__fin = 0
        self.__n = n
    
    
    def insert(self, e):
        if(self.__fin == self.__n):
            print("Cola llena")
        else:
            self.__fin = self.__fin + 1
            self.__arreglo[self.__fin] = e

    def remove(self):
        if(self.__inicio == 0 and self.__fin == 0):
            print("Cola vacia")
            return None
        else:
            self.__inicio = self.__inicio+1
            dato = self.__arreglo[self.__inicio]
            if(self.__inicio == self.__fin):
                self.__inicio = 0
                self.__fin = 0
            return dato
    
    def peek(self):
        return self.__arreglo[self.__inicio+1]

    def isEmpty(self):
        if(self.__inicio == 0 and self.__fin == 0):
            return True
        else:
            return False
    
    def isFull(self):
        if(self.__fin == self.__n):
            return True
        else:
            return False
  
    def nroelem(self): # size
        aux = Cola(self.__n)
        contador = 0
        while(not self.isEmpty()):
            dato = self.remove()
            aux.insert(dato)
            contador = contador + 1
        
        while(not aux.isEmpty()):
            dato = aux.remove()
            self.insert(dato)        
        return contador



