"""
═══════════════════════════════════════════════════════════════
EXAMEN - MEMORIZACIÓN (DP)
═══════════════════════════════════════════════════════════════
"""

# PUNTO 1: FIBONACCI CON MEMO
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


# PUNTO 2: CAMINOS EN ESCALERA
memo2 = {}

def formas(n):
    if n in memo2:
        return memo2[n]
    if n <= 2:
        return n
    memo2[n] = formas(n-1) + formas(n-2)
    return memo2[n]


# PUNTO 3: SUMA SUBCONJUNTO
memo3 = {}

def subset(nums, target, i=0):
    if (i, target) in memo3:
        return memo3[(i, target)]

    if target == 0:
        return True
    if i >= len(nums) or target < 0:
        return False

    res = subset(nums, target-nums[i], i+1) or subset(nums, target, i+1)
    memo3[(i, target)] = res
    return res


# PRUEBA
if __name__ == "__main__":
    print(fib(10))
    print(formas(5))
    print(subset([3, 2, 7, 1], 6))