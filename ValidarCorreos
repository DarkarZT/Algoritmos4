import re

def validar_correo(correo: str) -> bool:
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

# Pruebas
correos = [
    "usuario@ejemplo.com",
    "nombre.apellido@dominio.org",
    "correo+filtro@empresa.co",
    "invalido@",
    "@sinusuario.com",
    "sinArroba.com",
    "doble@@dominio.com",
]

for correo in correos:
    estado = "✅ válido" if validar_correo(correo) else "❌ inválido"
    print(f"{estado}: {correo}")
