usuarios_activos = {"Ana", "Luis", "Pedro", "Maria", "Sofia", "Juan"}
usuarios_premium = {"Pedro", "Sofia", "Carlos", "Laura"}
usuarios_bloqueados = {"Juan", "Carlos"}

asistencia_lunes = {"Ana", "Luis", "Pedro", "Maria"}
asistencia_martes = {"Ana", "Sofia", "Pedro", "Juan"}
asistencia_miercoles = {"Luis", "Pedro", "Sofia", "Carlos"}


def usuarios_que_son_activos_y_premium():
    return usuarios_activos & usuarios_premium


def usuarios_activos_no_bloqueados():
    return usuarios_activos - usuarios_bloqueados


def estudiantes_perfectos():
    return asistencia_lunes & asistencia_martes & asistencia_miercoles


def estudiantes_faltaron_al_menos_un_dia():
    todos = asistencia_lunes | asistencia_martes | asistencia_miercoles
    return todos - estudiantes_perfectos()


def dia_con_mas_asistencia():
    dias = {
        "lunes": asistencia_lunes,
        "martes": asistencia_martes,
        "miercoles": asistencia_miercoles
    }
    return max(dias, key=lambda d: len(dias[d]))


# PRUEBAS
print(usuarios_que_son_activos_y_premium())
print(estudiantes_perfectos())
print(dia_con_mas_asistencia())
