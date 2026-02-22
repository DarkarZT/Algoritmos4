def permutacionRecursiva(arreglo, inicio, fin):
    if inicio == fin:
        print(arreglo)
    else:
        for i in range(inicio, fin + 1):
            arreglo[inicio], arreglo[i] = arreglo[i], arreglo[inicio]
            permutacionRecursiva(arreglo, inicio + 1, fin)
            arreglo[inicio], arreglo[i] = arreglo[i], arreglo[inicio]