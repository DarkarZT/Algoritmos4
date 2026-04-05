"""
═══════════════════════════════════════════════════════════════
EXAMEN - LISTA DE TAREAS
═══════════════════════════════════════════════════════════════
"""

# PUNTO 1: NODO
class Nodo:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.sig = None


# PUNTO 2: LISTA
class ListaTareas:
    def __init__(self):
        self.head = None

    # AGREGAR RECURSIVO
    def agregar(self, desc, prioridad):
        self.head = self._agregar(self.head, desc, prioridad)

    def _agregar(self, nodo, desc, prioridad):
        if nodo is None or prioridad > nodo.prioridad:
            nuevo = Nodo(desc, prioridad)
            nuevo.sig = nodo
            return nuevo

        nodo.sig = self._agregar(nodo.sig, desc, prioridad)
        return nodo

    # CONTAR PENDIENTES
    def contar_pendientes(self, prioridad):
        return self._contar(self.head, prioridad)

    def _contar(self, nodo, prioridad):
        if nodo is None:
            return 0
        count = 1 if (not nodo.completada and nodo.prioridad == prioridad) else 0
        return count + self._contar(nodo.sig, prioridad)

    # OBTENER URGENTES
    def obtener_urgentes(self):
        nueva = ListaTareas()
        self._urgentes(self.head, nueva)
        return nueva

    def _urgentes(self, nodo, nueva):
        if nodo is None:
            return
        if not nodo.completada and nodo.prioridad >= 4:
            nueva.agregar(nodo.descripcion, nodo.prioridad)
        self._urgentes(nodo.sig, nueva)

    # LIMPIAR COMPLETADAS
    def limpiar_completadas(self):
        self.head = self._limpiar(self.head)

    def _limpiar(self, nodo):
        if nodo is None:
            return None
        nodo.sig = self._limpiar(nodo.sig)
        if nodo.completada:
            return nodo.sig
        return nodo

    # MOSTRAR
    def mostrar(self):
        actual = self.head
        while actual:
            estado = "✓" if actual.completada else "○"
            print(f"[{estado}] {actual.descripcion} ({actual.prioridad})")
            actual = actual.sig

if __name__ == "__main__":
    print("=" * 50)
    print("PRUEBA LISTA DE TAREAS")
    print("=" * 50)

    lista = ListaTareas()

    # AGREGAR TAREAS
    lista.agregar("Comprar leche", 2)
    lista.agregar("Estudiar", 5)
    lista.agregar("Hacer ejercicio", 3)
    lista.agregar("Dormir", 1)
    lista.agregar("Proyecto", 5)

    print("\n📋 Lista inicial:")
    lista.mostrar()

    # CONTAR
    print("\n🔢 Pendientes prioridad 5:", lista.contar_pendientes(5))

    # MARCAR ALGUNAS COMO COMPLETADAS (manual)
    lista.head.completada = True  # marca la primera como completada

    print("\n📋 Después de completar una:")
    lista.mostrar()

    # URGENTES
    print("\n🚨 Urgentes:")
    urgentes = lista.obtener_urgentes()
    urgentes.mostrar()

    # LIMPIAR
    print("\n🗑️ Limpiando completadas...")
    lista.limpiar_completadas()

    print("\n📋 Lista final:")
    lista.mostrar()