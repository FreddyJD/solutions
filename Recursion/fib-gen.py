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


def _fib_gen(n):
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
        yield first


# for num in _fib_gen(1000):
#     print(num)


"""
Generators / Yields / Dequeu
"""
from collections import deque

def fib_gen(num):
    memory = deque([0, 1], maxlen = 2)
    for _ in range(num - 1):
        memory.append(memory[0] + memory[-1])
        yield memory[-1]


# print(list(fib_num))
fib_num = fib_gen(10)
print(int(next(fib_num)))
print(int(next(fib_num)))
print(int(next(fib_num)))
print(int(next(fib_num)))
print(int(next(fib_num)))
print(int(next(fib_num)))

###########################
def _fib_gen(n):
    first = 0
    second = 1

    for _ in range(n):
        first, second = second, first + second

    return first

# print(_fib_gen(1))
# print(_fib_gen(2))
# print(_fib_gen(3))
# print(_fib_gen(4))
# print(_fib_gen(5))
# print(_fib_gen(6))
# print(_fib_gen(7))