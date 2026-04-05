"""
═══════════════════════════════════════════════════════════════
EXAMEN 1 - SISTEMA DE CONTACTOS
═══════════════════════════════════════════════════════════════
"""

import re

# NODO
class Nodo:
    def __init__(self, nombre, telefono, intereses):
        self.nombre = nombre
        self.telefono = telefono
        self.intereses = set(intereses)
        self.sig = None


# LISTA
class ListaContactos:
    def __init__(self):
        self.head = None

    # VALIDAR TELÉFONO (regex)
    def telefono_valido(self, tel):
        return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', tel))

    # AGREGAR (RECURSIVO)
    def agregar(self, nombre, telefono, intereses):
        if not self.telefono_valido(telefono):
            return
        self.head = self._agregar(self.head, nombre, telefono, intereses)

    def _agregar(self, nodo, nombre, telefono, intereses):
        if nodo is None:
            return Nodo(nombre, telefono, intereses)
        nodo.sig = self._agregar(nodo.sig, nombre, telefono, intereses)
        return nodo

    # CONTAR CONTACTOS CON INTERÉS
    def contar_interes(self, interes):
        return self._contar(self.head, interes)

    def _contar(self, nodo, interes):
        if nodo is None:
            return 0
        c = 1 if interes in nodo.intereses else 0
        return c + self._contar(nodo.sig, interes)

    # SUGERIR CONTACTOS (CONJUNTOS)
    def sugerencias(self, intereses_usuario):
        res = set()
        self._sugerencias(self.head, intereses_usuario, res)
        return res

    def _sugerencias(self, nodo, intereses_usuario, res):
        if nodo is None:
            return
        if nodo.intereses & intereses_usuario:
            res.add(nodo.nombre)
        self._sugerencias(nodo.sig, intereses_usuario, res)

    # MEMO: SIMILITUD ENTRE CONTACTOS
    memo = {}

    def similitud(self, c1, c2):
        key = (c1.nombre, c2.nombre)
        if key in self.memo:
            return self.memo[key]
        inter = c1.intereses & c2.intereses
        union = c1.intereses | c2.intereses
        val = len(inter)/len(union) if union else 0
        self.memo[key] = val
        return val

    # MOSTRAR
    def mostrar(self):
        a = self.head
        while a:
            print(a.nombre, a.telefono, a.intereses)
            a = a.sig


# PRUEBA
if __name__ == "__main__":
    l = ListaContactos()
    l.agregar("Ana", "300-123-4567", {"ia","python"})
    l.agregar("Luis", "301-555-9999", {"web","python"})

    l.mostrar()
    print("Interes python:", l.contar_interes("python"))
    print("Sugerencias:", l.sugerencias({"python"}))