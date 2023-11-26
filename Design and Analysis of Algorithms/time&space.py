import timeit

def non_recursive_fibonacci(n):
    """Calculate Fibonacci using a non-recursive approach."""
    if n <= 1:
        return n

    fib_list = [0] * (n + 1)
    fib_list[1] = 1

    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

    return fib_list[n]

def recursive_fibonacci(n):
    """Calculate Fibonacci using a recursive approach."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

N = int(input("Enter the value of N: "))

print(f"Given N = {N}")

# Non-Recursive Fibonacci
non_recursive_time = timeit.timeit("non_recursive_fibonacci(N)", globals=globals())
non_recursive_result = non_recursive_fibonacci(N)
print(f"Non-Recursive Fibonacci for N = {N}: {non_recursive_result}")
print(f"Time Complexity: {non_recursive_time:.5f} seconds (O(n))\nSpace Complexity: O(n)")

# Print the Non-Recursive Fibonacci series
print(f"Fibonacci series for N = {N}:")
for i in range(N + 1):
    print(non_recursive_fibonacci(i), end=" ")

print("\n")

# Recursive Fibonacci
recursive_time = timeit.timeit("recursive_fibonacci(N)", globals=globals())
recursive_result = recursive_fibonacci(N)
print(f"Recursive Fibonacci for N = {N}: {recursive_result}")
print(f"Time Complexity: {recursive_time:.5f} seconds (O(2^n))\nSpace Complexity: O(n)")

# Print the Recursive Fibonacci series
print(f"Fibonacci series for N = {N}:")
for i in range(N + 1):
    print(recursive_fibonacci(i), end=" ")