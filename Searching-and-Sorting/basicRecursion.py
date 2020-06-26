def fibonacci(n):

    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# test cases
print(fibonacci(9))
print(fibonacci(11))
print(fibonacci(0))
