
def fibonacci(n):
    # fib(n) = fib(n-1) + fib(n-2)

    # Define base/stopping case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive call
    fib = fibonacci(n-1) + fibonacci(n-2) 
    return fib


res = fibonacci(30)
print(res)