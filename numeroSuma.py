def sumaDelosNumeros(a):
    if a // 10 == 0:
        return a
    else:
        return (a % 10) + sumaDelosNumeros(a // 10)
    
print(sumaDelosNumeros(1503))

    