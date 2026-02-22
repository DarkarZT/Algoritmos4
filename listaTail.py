# =========================
# CLASE NODO
# =========================
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# =========================
# CLASE LISTA ENLAZADA
# =========================
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None


    # =========================
    # AGREGAR AL INICIO
    # =========================
    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo


    # =========================
    # AGREGAR AL FINAL (TAIL)
    # =========================
    def agregar_final(self, dato):
        def _agregar(nodo, nuevo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
                return
            return _agregar(nodo.siguiente, nuevo)

        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            _agregar(self.cabeza, nuevo)


    # =========================
    # MOSTRAR (TAIL)
    # =========================
    def mostrar(self):
        def _mostrar(nodo):
            if nodo is None:
                print("None")
                return
            print(nodo.dato, end=" -> ")
            return _mostrar(nodo.siguiente)

        _mostrar(self.cabeza)


    # =========================
    # ELIMINAR (TAIL)
    # =========================
    def eliminar(self, dato):
        def _eliminar(nodo, anterior):
            if nodo is None:
                return

            if nodo.dato == dato:
                if anterior is None:
                    self.cabeza = nodo.siguiente
                else:
                    anterior.siguiente = nodo.siguiente
                return

            return _eliminar(nodo.siguiente, nodo)

        _eliminar(self.cabeza, None)


    # =========================
    # TAMAÑO (TAIL)
    # =========================
    def tamano(self):
        def _tamano(nodo, acc=0):
            if nodo is None:
                return acc
            return _tamano(nodo.siguiente, acc+1)

        return _tamano(self.cabeza)


    # =========================
    # REVERSAR (TAIL)
    # =========================
    def reversar(self):
        def _reversar(nodo, previo=None):
            if nodo is None:
                return previo
            siguiente = nodo.siguiente
            nodo.siguiente = previo
            return _reversar(siguiente, nodo)

        self.cabeza = _reversar(self.cabeza)


    # =========================
    # INSERTAR EN POSICION (TAIL)
    # =========================
    def insertar(self, dato, pos):
        def _insertar(nodo, i):
            if nodo is None:
                return
            if i == pos-1:
                nuevo.siguiente = nodo.siguiente
                nodo.siguiente = nuevo
                return
            return _insertar(nodo.siguiente, i+1)

        nuevo = Nodo(dato)

        if pos == 0:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            _insertar(self.cabeza, 0)


    # =========================
    # BUSQUEDA POR VALOR (TAIL)
    # =========================
    def buscar_recursivo(self, dato):
        def _buscar(nodo):
            if nodo is None:
                return False
            if nodo.dato == dato:
                return True
            return _buscar(nodo.siguiente)

        return _buscar(self.cabeza)


    # =========================
    # BUSQUEDA POR INDICE (TAIL)
    # =========================
    def buscar_por_indice(self, index):
        def _buscar(nodo, i):
            if nodo is None:
                return None
            if i == index:
                return nodo.dato
            return _buscar(nodo.siguiente, i+1)

        return _buscar(self.cabeza, 0)


    # =========================
    # BUSCAR POSICION POR VALOR (TAIL)
    # =========================
    def buscar_posicion(self, dato):
        def _buscar(nodo, i):
            if nodo is None:
                return -1
            if nodo.dato == dato:
                return i
            return _buscar(nodo.siguiente, i+1)

        return _buscar(self.cabeza, 0)



# =========================
# MAIN (EJECUCION)
# =========================
if __name__ == "__main__":

    lista = ListaEnlazada()

    lista.agregar_inicio(1)
    lista.agregar_final(2)
    lista.agregar_final(3)
    lista.agregar_final(4)

    print("Lista:")
    lista.mostrar()

    print("\nTamaño:", lista.tamano())

    print("\nBusqueda de 3:", lista.buscar_recursivo(3))
    print("Dato en indice 2:", lista.buscar_por_indice(2))
    print("Posicion del 4:", lista.buscar_posicion(4))

    lista.eliminar(2)
    print("\nEliminar 2:")
    lista.mostrar()

    lista.insertar(99, 2)
    print("\nInsertar 99 en posicion 2:")
    lista.mostrar()

    lista.reversar()
    print("\nReversa:")
    lista.mostrar()