roles = {"admin":{"leer","escribir","eliminar","crear_usuario","ver_logs","configurar","backup","restaurar"},"editor":{"leer","escribir","Subir_archivos"},"viewer":{"leer"},"moderador":{"leer","escribir","eliminar","ver_logs"}, "auditor":{"leer","ver_logs","exportar_reportes"}}

usuarios = {"alice":"admin","bob":"editor","charlie":"viewer","dave":"moderador","eve":"auditor"}


def verificar_permiso(usuario, permiso):
    rol = usuarios.get (usuario)
    print(rol,"oli")
    if rol:
        permisos = roles.get(rol, set())
        print(permisos,"oliwis")
        if permiso in permisos:
            return print("Si tiene ese permiso")
        else:
            return print("no tiene ese permiso")
    return print("el usuario no existe")

def valida

verificar_permiso("dave","bellakear")