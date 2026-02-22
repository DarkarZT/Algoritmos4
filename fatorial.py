def factorial(n):
    if n <= 1:
        print (f"Caso base alcanzado {n} = 1")
        return 1
    total = n*factorial(n-1)
    print (total)
    return total
    
factorial(5)