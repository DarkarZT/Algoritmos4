import re

# ---------------- REGEX ----------------

def validar_correo_universitario(correo):
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@universidad\.edu\.co$", correo))


def extraer_telefonos(texto):
    return re.findall(r"\b(?:3\d{9}|601\d{7}|\d{3}-\d{3}-\d{4})\b", texto)


# ---------------- CONJUNTOS ----------------

programacion = {"Ana", "Luis", "Pedro", "Maria"}
matematicas = {"Pedro", "Sofia", "Carlos", "Ana"}
fisica = {"Luis", "Carlos", "Sofia"}


def estudiantes_todas_materias():
    return programacion & matematicas & fisica


def estudiantes_solo_una_materia():
    todos = programacion | matematicas | fisica
    return {
        e for e in todos
        if sum([
            e in programacion,
            e in matematicas,
            e in fisica
        ]) == 1
    }


def estudiantes_en_dos_materias_exactas():
    todos = programacion | matematicas | fisica
    return {
        e for e in todos
        if sum([
            e in programacion,
            e in matematicas,
            e in fisica
        ]) == 2
    }


# ---------------- LISTA ENLAZADA ----------------

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.siguiente = None


class Carrito:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, nombre, precio, cantidad):

        nuevo = Producto(nombre, precio, cantidad)

        def insertar(nodo):
            if nodo is None:
                return nuevo
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                insertar(nodo.siguiente)
            return nodo

        self.cabeza = insertar(self.cabeza)

    def total_compra(self):

        def sumar(nodo):
            if nodo is None:
                return 0
            return (nodo.precio * nodo.cantidad) + sumar(nodo.siguiente)

        return sumar(self.cabeza)

    def eliminar_productos_baratos(self, limite):

        def filtrar(nodo):
            if nodo is None:
                return None

            nodo.siguiente = filtrar(nodo.siguiente)

            if nodo.precio < limite:
                return nodo.siguiente
            return nodo

        self.cabeza = filtrar(self.cabeza)


# PRUEBA FINAL
carrito = Carrito()
carrito.agregar_producto("Mouse", 50, 2)
carrito.agregar_producto("Teclado", 120, 1)
carrito.agregar_producto("Cable", 10, 3)

print("Total:", carrito.total_compra())
