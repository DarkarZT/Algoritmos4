class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class Lista():
    def __init__(self):
        self.cabeza = None
        
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    def longitudRecursiva(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self.longitudRecursiva(nodo.siguiente)
    def encontrarDato(self, nodo, dato):
        if nodo is None:
            return False
        elif nodo.dato  == dato:
            return True 
        return self.encontrarDato(nodo.siguiente, dato)
        
lista = Lista()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
print(lista.longitudRecursiva(lista.cabeza))