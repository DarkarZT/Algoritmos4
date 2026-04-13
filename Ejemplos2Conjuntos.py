stock_tienda = {"lapiz", "cuaderno", "borrador", "regla"}
stock_bodega = {"cuaderno", "regla", "colores", "marcador"}
stock_proveedores = {"lapiz", "tinta", "colores"}


def productos_disponibles_en_todos():
    return stock_tienda & stock_bodega & stock_proveedores


def productos_exclusivos_tienda():
    return stock_tienda - stock_bodega - stock_proveedores


class Turno:
    def __init__(self, cliente, tipo, prioridad=False):
        self.cliente = cliente
        self.tipo = tipo
        self.prioridad = prioridad
        self.siguiente = None


class ListaTurnos:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        while actual:
            estado = "⭐" if actual.prioridad else "○"
            print(estado, actual.cliente, actual.tipo)
            actual = actual.siguiente

    def agregar_turno(self, cliente, tipo, prioridad):

        nuevo = Turno(cliente, tipo, prioridad)

        def insertar(nodo):
            if nodo is None:
                return nuevo
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                insertar(nodo.siguiente)
            return nodo

        self.cabeza = insertar(self.cabeza)

    def contar_prioritarios(self):

        def contar(nodo):
            if nodo is None:
                return 0
            return (1 if nodo.prioridad else 0) + contar(nodo.siguiente)

        return contar(self.cabeza)

    def eliminar_no_prioritarios(self):

        def filtrar(nodo):
            if nodo is None:
                return None

            nodo.siguiente = filtrar(nodo.siguiente)

            if not nodo.prioridad:
                return nodo.siguiente
            return nodo

        self.cabeza = filtrar(self.cabeza)


# PRUEBA
lista = ListaTurnos()
lista.agregar_turno("Ana", "Caja", True)
lista.agregar_turno("Luis", "Consulta", False)
lista.agregar_turno("Pedro", "Caja", True)

lista.mostrar()
print("Prioritarios:", lista.contar_prioritarios())
