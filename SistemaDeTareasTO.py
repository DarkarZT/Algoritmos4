"""
═══════════════════════════════════════════════════════════════
EXAMEN 2 - TAREAS AVANZADAS
═══════════════════════════════════════════════════════════════
"""

import re

class Nodo:
    def __init__(self, desc, prioridad, etiquetas):
        self.desc = desc
        self.prioridad = prioridad
        self.etiquetas = set(etiquetas)
        self.completada = False
        self.sig = None


class Lista:
    def __init__(self):
        self.head = None

    # VALIDAR TEXTO (regex: sin números)
    def validar(self, texto):
        return not re.search(r'\d', texto)

    # AGREGAR ORDENADO (recursivo)
    def agregar(self, desc, prioridad, etiquetas):
        if not self.validar(desc):
            return
        self.head = self._agregar(self.head, desc, prioridad, etiquetas)

    def _agregar(self, nodo, desc, prioridad, etiquetas):
        if nodo is None or prioridad > nodo.prioridad:
            nuevo = Nodo(desc, prioridad, etiquetas)
            nuevo.sig = nodo
            return nuevo
        nodo.sig = self._agregar(nodo.sig, desc, prioridad, etiquetas)
        return nodo

    # CONTAR POR ETIQUETA
    def contar(self, etiqueta):
        return self._contar(self.head, etiqueta)

    def _contar(self, nodo, etiqueta):
        if nodo is None:
            return 0
        c = 1 if etiqueta in nodo.etiquetas else 0
        return c + self._contar(nodo.sig, etiqueta)

    # OBTENER TAREAS SIMILARES (conjuntos)
    def similares(self, etiquetas):
        res = []
        self._similares(self.head, etiquetas, res)
        return res

    def _similares(self, nodo, etiquetas, res):
        if nodo is None:
            return
        if nodo.etiquetas & etiquetas:
            res.append(nodo.desc)
        self._similares(nodo.sig, etiquetas, res)

    # MEMO: COSTO (tipo fibonacci)
    memo = {}
    def costo(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return 1
        self.memo[n] = self.costo(n-1) + self.costo(n-2)
        return self.memo[n]

    def mostrar(self):
        a = self.head
        while a:
            print(a.desc, a.prioridad, a.etiquetas)
            a = a.sig


# PRUEBA
if __name__ == "__main__":
    l = Lista()
    l.agregar("Estudiar",5,{"uni"})
    l.agregar("Gym",3,{"salud"})

    l.mostrar()
    print("Contar:", l.contar("uni"))
    print("Similares:", l.similares({"uni"}))
    print("Costo:", l.costo(5))