def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

n = int(input("Enter a number: "))
result = fibonacci_non_recursive(n)
print(f"The {n}-th Fibonacci number is {result}")
