"""
@Math.Factorial
"""
import math
print(math.factorial(23))


"""
@Factorial with Recursion
"""


def _factorial(n):
    if n == 1:
        return n
    else:
        return n * _factorial(n - 1)

print(_factorial(23))


"""
@Factorial Iterative
"""
n = 23
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)
