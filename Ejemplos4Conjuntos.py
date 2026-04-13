# =========================
# CONJUNTOS
# =========================

programacion = {"Ana", "Luis", "Pedro", "Maria"}
matematicas = {"Pedro", "Sofia", "Carlos", "Ana"}
fisica = {"Luis", "Carlos", "Sofia", "David"}


def en_todas_las_materias():
    return programacion & matematicas & fisica


def en_al_menos_una():
    return programacion | matematicas | fisica


def en_una_sola_materia():
    todos = programacion | matematicas | fisica
    return {
        e for e in todos
        if sum([
            e in programacion,
            e in matematicas,
            e in fisica
        ]) == 1
    }


def sin_matematicas():
    return (programacion | fisica) - matematicas


# =========================
# LISTA ENLAZADA
# =========================

class Pedido:
    def __init__(self, cliente, valor, entregado=False):
        self.cliente = cliente
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    # agregar (recursivo)
    def agregar(self, cliente, valor, entregado=False):
        nuevo = Pedido(cliente, valor, entregado)

        def insertar(nodo):
            if nodo is None:
                return nuevo
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                insertar(nodo.siguiente)
            return nodo

        self.cabeza = insertar(self.cabeza)

    # mostrar
    def mostrar(self):
        actual = self.cabeza
        while actual:
            estado = "✔" if actual.entregado else "○"
            print(f"{estado} {actual.cliente} - ${actual.valor}")
            actual = actual.siguiente

    # sumar no entregados (recursivo)
    def valor_pendiente(self):
        def sumar(nodo):
            if nodo is None:
                return 0
            if not nodo.entregado:
                return nodo.valor + sumar(nodo.siguiente)
            return sumar(nodo.siguiente)

        return sumar(self.cabeza)

    # contar entregados
    def contar_entregados(self):
        def contar(nodo):
            if nodo is None:
                return 0
            return (1 if nodo.entregado else 0) + contar(nodo.siguiente)

        return contar(self.cabeza)

    # eliminar entregados (recursivo)
    def eliminar_entregados(self):
        def filtrar(nodo):
            if nodo is None:
                return None

            nodo.siguiente = filtrar(nodo.siguiente)

            if nodo.entregado:
                return nodo.siguiente
            return nodo

        self.cabeza = filtrar(self.cabeza)


# =========================
# PRUEBA GENERAL
# =========================

print("CONJUNTOS:")
print(en_todas_las_materias())
print(en_al_menos_una())
print(en_una_sola_materia())
print(sin_matematicas())

print("\nLISTA ENLAZADA:")
lista = ListaPedidos()
lista.agregar("Ana", 10000, False)
lista.agregar("Luis", 20000, True)
lista.agregar("Pedro", 15000, False)

lista.mostrar()
print("Pendiente:", lista.valor_pendiente())
print("Entregados:", lista.contar_entregados())
