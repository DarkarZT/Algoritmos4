# ===============================
# 4. Potencia
# ===============================
def power(base, exp, acc=1):
    if exp == 0:
        return acc
    return power(base, exp-1, acc*base)

print("2^5:", power(2,5))


# ===============================
# 5. Máximo de Lista
# ===============================
def max_list(lst, current=None):
    if not lst:
        return current
    if current is None or lst[0] > current:
        current = lst[0]
    return max_list(lst[1:], current)

print("Max:", max_list([3,7,2,9,5]))


# ===============================
# 6. Reversa de Lista
# ===============================
def reverse_list(lst, acc=None):
    if acc is None:
        acc = []
    if not lst:
        return acc
    return reverse_list(lst[1:], [lst[0]] + acc)

print("Reversa:", reverse_list([1,2,3,4]))


# ===============================
# 7. Contar Ocurrencias
# ===============================
def count(lst, target, acc=0):
    if not lst:
        return acc
    if lst[0] == target:
        acc += 1
    return count(lst[1:], target, acc)

print("Ocurrencias de 2:", count([2,3,2,4,2,5],2))


# ===============================
# 8. Producto de Lista
# ===============================
def product(lst, acc=1):
    if not lst:
        return acc
    return product(lst[1:], acc*lst[0])

print("Producto:", product([1,2,3,4]))


# ===============================
# 9. GCD (Euclides)
# ===============================
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD(48,18):", gcd(48,18))


# ===============================
# 10. Decimal a Binario
# ===============================
def to_binary(n, acc=""):
    if n == 0:
        return acc or "0"
    return to_binary(n//2, str(n%2) + acc)

print("Binario de 10:", to_binary(10))