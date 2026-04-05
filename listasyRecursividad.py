"""
═══════════════════════════════════════════════════════════════
EXAMEN - LISTA ENLAZADA AVANZADA
═══════════════════════════════════════════════════════════════
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class Lista:
    def __init__(self):
        self.head = None

    # INSERTAR AL FINAL (RECURSIVO)
    def insertar(self, valor):
        self.head = self._insertar(self.head, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        nodo.sig = self._insertar(nodo.sig, valor)
        return nodo

    # SUMAR ELEMENTOS (RECURSIVO)
    def suma(self):
        return self._suma(self.head)

    def _suma(self, nodo):
        if nodo is None:
            return 0
        return nodo.valor + self._suma(nodo.sig)

    # CONTAR NODOS
    def contar(self):
        return self._contar(self.head)

    def _contar(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar(nodo.sig)

    # INVERTIR LISTA (RECURSIVO)
    def invertir(self):
        self.head = self._invertir(self.head)

    def _invertir(self, nodo):
        if nodo is None or nodo.sig is None:
            return nodo
        nueva = self._invertir(nodo.sig)
        nodo.sig.sig = nodo
        nodo.sig = None
        return nueva

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.sig
        print("None")


# PRUEBA
if __name__ == "__main__":
    l = Lista()
    for i in [1, 2, 3, 4]:
        l.insertar(i)

    l.mostrar()
    print("Suma:", l.suma())
    print("Cantidad:", l.contar())

    l.invertir()
    l.mostrar()