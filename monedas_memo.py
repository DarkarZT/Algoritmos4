def cambio(cantidad, monedas):
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')
    
    minimo = float('inf')
    
    for moneda in monedas:
        resultado = cambio(cantidad-moneda, monedas)
        minimo = min(resultado + 1, minimo)
        
    return minimo

def cambio_memo(cantidad, monedas, diccionario={}):
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')
    
    for moneda in range(1, monedas.len()):
        if moneda in diccionario:
            resultado = diccionario[moneda]
        
    minimo = float('inf')
    
    