def potenciaTail(base, exponente, resultado=1):
    if exponente == 0:
        return resultado
    else:
        return potenciaTail(base, exponente - 1, resultado * base)
    
print(potenciaTail(2, 3))