def busquedaBinariaRecursiva(arreglo, valor, inicio, fin):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if arreglo[medio] == valor:
        return medio
    elif arreglo[medio] < valor:
        return busquedaBinariaRecursiva(arreglo, valor, medio + 1, fin)
    else:
        return busquedaBinariaRecursiva(arreglo, valor, inicio, medio - 1)