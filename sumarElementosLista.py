import time

def tailSumalista(lista, n):
    if n == 0:
        return 0
    else:
        return lista[n - 1] + tailSumalista(lista, n - 1)
                  
                  
inicio = time.time()
lista = [1, 2, 3, 4, 5]
fin = time.time()                  
                  
                  
print("Tiempo de ejecución:", fin - inicio, "segundos")