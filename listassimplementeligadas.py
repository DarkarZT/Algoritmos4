class Nodo:
    def __init__(self,nombre,cedula, prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.prioridad = prioridad
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    """ def CrearNodo(self,Nombre,Cedula):
        nodo = Nodo(Nombre,Cedula)
        
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nodo """
    def MostrarLista(self):
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                print(f"Nombre: {actual.nombre}, Cédula: {actual.cedula}")
                actual = actual.siguiente
                
    def AgregarSegunPrioridad(self,Nombre,Cedula,Prioridad):
        nodo = Nodo(Nombre,Cedula,Prioridad)
        
        if self.cabeza == None or self.cabeza.prioridad > Prioridad:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None and actual.siguiente.prioridad <= Prioridad:
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo
            
lista = Lista()

lista.AgregarSegunPrioridad("juan perez","12312312",1)
lista.AgregarSegunPrioridad("Pepe","5431221",2)
lista.AgregarSegunPrioridad("Maria Gomez","98765432",3)
lista.AgregarSegunPrioridad("Pacho","98765432",1)

lista.MostrarLista()