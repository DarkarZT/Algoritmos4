"""
═══════════════════════════════════════════════════════════════
EXAMEN - VALIDACIÓN DE DATOS (REGEX)
═══════════════════════════════════════════════════════════════
"""

import re

# PUNTO 1: VALIDAR EMAIL
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))


# PUNTO 2: EXTRAER TELÉFONOS (formato: 300-123-4567)
def extraer_telefonos(texto):
    patron = r'\d{3}-\d{3}-\d{4}'
    return re.findall(patron, texto)


# PUNTO 3: VALIDAR CONTRASEÑA
# mínimo 8 caracteres, 1 mayúscula, 1 número
def validar_password(p):
    patron = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(patron, p))


# PUNTO 4: REEMPLAZAR NÚMEROS POR '*'
def ocultar_numeros(texto):
    return re.sub(r'\d', '*', texto)


# PUNTO 5: EXTRAER PALABRAS QUE EMPIEZAN EN MAYÚSCULA
def palabras_mayus(texto):
    return re.findall(r'\b[A-Z][a-z]*\b', texto)


# PRUEBA
if __name__ == "__main__":
    print(validar_email("test@gmail.com"))
    print(extraer_telefonos("Llama al 300-123-4567 o 301-555-9999"))
    print(validar_password("Hola1234"))
    print(ocultar_numeros("Mi clave es 1234"))
    print(palabras_mayus("Hola Mundo desde Python"))