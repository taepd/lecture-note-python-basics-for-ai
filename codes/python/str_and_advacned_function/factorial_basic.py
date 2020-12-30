def factorial(n):
    result = 1
    for idx in range(1, n + 1):
        result = result * idx
    return result


print(factorial(6))
