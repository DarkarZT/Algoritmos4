# ============================================================
# APUNTES COMPLETOS - REGEX, CONJUNTOS, LISTAS, RECURSIVIDAD
# ============================================================

import re
from functools import lru_cache

print("="*50)
print("1. EXPRESIONES REGULARES")
print("="*50)

texto = "Hola, mi correo es test@gmail.com y mi número es 300-123-4567"

# MATCH
print("match:", bool(re.match(r"Hola", texto)))

# SEARCH
print("search:", bool(re.search(r"correo", texto)))

# FINDALL
print("números:", re.findall(r"\d+", texto))

# SPLIT
print("split:", re.split(r"\s", texto)[:5])

# SUB
print("ocultar números:", re.sub(r"\d", "*", texto))

# VALIDACIONES
print("email válido:", bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', "test@gmail.com")))
print("tel válido:", bool(re.match(r'^\d{3}-\d{3}-\d{4}$', "300-123-4567")))


# ============================================================
print("\n" + "="*50)
print("2. CONJUNTOS")
print("="*50)

A = {1,2,3}
B = {3,4,5}

print("Unión:", A | B)
print("Intersección:", A & B)
print("Diferencia A-B:", A - B)
print("Simétrica:", A ^ B)

print("Subconjunto:", A <= B)
print("Disjuntos:", A.isdisjoint(B))

# Métodos
A.add(10)
A.discard(99)
print("A modificado:", A)

# eliminar duplicados
lista = [1,1,2,2,3]
print("Sin duplicados:", list(set(lista)))


# ============================================================
print("\n" + "="*50)
print("3. LISTA ENLAZADA")
print("="*50)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None

class Lista:
    def __init__(self):
        self.head = None

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.head:
            self.head = nuevo
            return
        actual = self.head
        while actual.sig:
            actual = actual.sig
        actual.sig = nuevo

    def eliminar(self, valor):
        if not self.head:
            return
        if self.head.valor == valor:
            self.head = self.head.sig
            return
        actual = self.head
        while actual.sig:
            if actual.sig.valor == valor:
                actual.sig = actual.sig.sig
                return
            actual = actual.sig

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.sig
        print("None")


# prueba lista
l = Lista()
l.insertar_final(1)
l.insertar_final(2)
l.insertar_final(3)

print("Lista:")
l.mostrar()

l.eliminar(2)
print("Después de eliminar 2:")
l.mostrar()


# ============================================================
print("\n" + "="*50)
print("4. RECURSIVIDAD")
print("="*50)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def suma(lista):
    if not lista:
        return 0
    return lista[0] + suma(lista[1:])

print("Factorial 5:", factorial(5))
print("Suma:", suma([1,2,3,4]))


# ============================================================
print("\n" + "="*50)
print("5. MEMORIZACIÓN")
print("="*50)

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

@lru_cache(None)
def fib2(n):
    if n <= 1:
        return n
    return fib2(n-1) + fib2(n-2)

print("Fib memo:", fib(10))
print("Fib cache:", fib2(10))


# ============================================================
print("\n" + "="*50)
print("FIN DEL ARCHIVO - TODO FUNCIONANDO")
print("="*50)