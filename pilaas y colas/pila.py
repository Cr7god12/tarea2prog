class Pila:
    def __init__(self, n):
        self.top = 0
        self.n = n
        self.arreglo = [0] * (n + 1)
    
    def push(self, e):
        if self.top == self.n:
            print("Pila llena")
        else:
            self.top = self.top + 1
            self.arreglo[self.top] = e
    
    def pop(self):
        if self.top == 0:
            print("Pila vacia")
            return 0
        else:
            dato = self.arreglo[self.top]
            self.top = self.top - 1
            return dato
    
    def peek(self):
        return self.arreglo[self.top]
    
    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.top == self.n:
            return True
        else:
            return False
