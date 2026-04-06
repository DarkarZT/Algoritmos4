class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class pila:
    def __init__(self):
        self.pila = []
        self.tope = None

    def push(self,dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1
    def pop(self):
        if self.tope is None:
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato
    