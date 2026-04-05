"""
═══════════════════════════════════════════════════════════════
EXAMEN 3 - CONTENIDO DIGITAL
═══════════════════════════════════════════════════════════════
"""

import re

class Nodo:
    def __init__(self, titulo, tags):
        self.titulo = titulo
        self.tags = set(tags)
        self.sig = None


class Plataforma:
    def __init__(self):
        self.head = None

    # VALIDAR TITULO (solo letras y espacios)
    def valido(self, t):
        return bool(re.match(r'^[A-Za-z ]+$', t))

    # INSERTAR
    def agregar(self, titulo, tags):
        if not self.valido(titulo):
            return
        self.head = self._agregar(self.head, titulo, tags)

    def _agregar(self, nodo, titulo, tags):
        if nodo is None:
            return Nodo(titulo, tags)
        nodo.sig = self._agregar(nodo.sig, titulo, tags)
        return nodo

    # CONTAR TAG
    def contar(self, tag):
        return self._contar(self.head, tag)

    def _contar(self, nodo, tag):
        if nodo is None:
            return 0
        c = 1 if tag in nodo.tags else 0
        return c + self._contar(nodo.sig, tag)

    # RECOMENDAR (conjuntos)
    def recomendar(self, intereses):
        res = set()
        self._rec(self.head, intereses, res)
        return res

    def _rec(self, nodo, intereses, res):
        if nodo is None:
            return
        if nodo.tags & intereses:
            res.add(nodo.titulo)
        self._rec(nodo.sig, intereses, res)

    # MEMO: similitud acumulada
    memo = {}
    def score(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = self.score(n-1) + self.score(n-2)
        return self.memo[n]

    def mostrar(self):
        a = self.head
        while a:
            print(a.titulo, a.tags)
            a = a.sig


# PRUEBA
if __name__ == "__main__":
    p = Plataforma()
    p.agregar("Python Basico", {"python","programacion"})
    p.agregar("IA Avanzada", {"ia","ml"})

    p.mostrar()
    print("Tag python:", p.contar("python"))
    print("Recomendado:", p.recomendar({"python"}))
    print("Score:", p.score(6))