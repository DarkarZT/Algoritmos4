"""
═══════════════════════════════════════════════════════════════
EXAMEN - CONTROL DE ACCESO
═══════════════════════════════════════════════════════════════
"""
# objetos
# PUNTO 1: CLASE ROL

class Rol:
    def __init__(self, nombre, permisos):
        self.nombre = nombre
        self.permisos = set(permisos)


class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol


# PUNTO 2: VERIFICAR ACCESO
def puede(usuario, acciones):
    return acciones <= usuario.rol.permisos


# PUNTO 3: PERMISOS COMUNES
def comunes(r1, r2):
    return r1.permisos & r2.permisos


# PUNTO 4: JERARQUÍA
def es_superior(r1, r2):
    return r2.permisos <= r1.permisos


# PUNTO 5: COMBINAR ROLES
def combinar(r1, r2):
    return r1.permisos | r2.permisos


# PRUEBA
if __name__ == "__main__":
    admin = Rol("admin", {"leer", "escribir", "eliminar"})
    user = Rol("user", {"leer"})

    juan = Usuario("Juan", admin)

    print(puede(juan, {"leer"}))
    print(comunes(admin, user))
    print(es_superior(admin, user))
    print(combinar(admin, user))