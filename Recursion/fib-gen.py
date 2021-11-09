"""
Fib sequence with memory outside of the function default
"""

memory = {}


def fib_memory(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n in memory:
        return memory[n]
    memory[n] = fib_memory(n - 1) + fib_memory(n - 2)
    return memory[n]


"""
Fib iterative solution that uses O(1) memory instead of O(n)
"""


def fib_iterative(n):
    first = 0
    second = 1

    for _ in range(n):
        first, second = second, first + second

    return first


"""
Fib with generator
"""


def fib_gen(n):
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
        yield first


for num in fib_gen(1000):
    print(num)
