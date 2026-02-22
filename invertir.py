def invertir(s):
    if len(s) <= 1:
        return s
    return invertir(s[1:]) + s[0]
    
prueba = invertir("hola")

print(prueba)