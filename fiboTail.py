def fib(n, a=0, b=1):
    if n == 0:
        return a
    return fib(n-1, b, a+b)

print("Fibonacci(10):", fib(10))