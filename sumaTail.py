def sum_n(n, acc=0):
    if n == 0:
        return acc
    return sum_n(n-1, acc+n)

print("Suma hasta 10:", sum_n(10))
