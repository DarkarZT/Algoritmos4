"""
═══════════════════════════════════════════════════════════════
EXAMEN - RED SOCIAL
═══════════════════════════════════════════════════════════════
"""
#objetos + conjuntos
# PUNTO 1: CLASE USUARIO

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = set()

    def agregar_amigo(self, otro):
        self.amigos.add(otro)

    def __repr__(self):
        return self.nombre


# PUNTO 2: AMIGOS EN COMÚN
def amigos_comunes(u1, u2):
    return u1.amigos & u2.amigos


# PUNTO 3: SUGERENCIAS
def sugerencias(usuario):
    sugeridos = set()
    for amigo in usuario.amigos:
        sugeridos |= amigo.amigos
    return sugeridos - usuario.amigos - {usuario}


# PUNTO 4: GRADO DE CONEXIÓN (JACCARD)
def grado_conexion(u1, u2):
    inter = u1.amigos & u2.amigos
    union = u1.amigos | u2.amigos
    return len(inter) / len(union) if union else 0


# PUNTO 5: USUARIO MÁS CONECTADO
def mas_conectado(usuarios):
    return max(usuarios, key=lambda u: len(u.amigos))


# PRUEBA
if __name__ == "__main__":
    ana = Usuario("Ana")
    luis = Usuario("Luis")
    carlos = Usuario("Carlos")

    ana.agregar_amigo(luis)
    ana.agregar_amigo(carlos)
    luis.agregar_amigo(carlos)

    print("Comunes:", amigos_comunes(ana, luis))
    print("Sugerencias:", sugerencias(ana))
    print("Grado:", grado_conexion(ana, luis))
    print("Más conectado:", mas_conectado([ana, luis, carlos]))