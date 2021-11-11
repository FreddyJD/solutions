import functools

n = 3
results = []


@functools.lru_cache
def generate_binary_strings(current):
    if len(current) == n:
        results.append(current)
        return

    generate_binary_strings(current + "0")
    generate_binary_strings(current + "1")


generate_binary_strings("")
print(results)

"""
https://www.keithschwarz.com/binary-subsets/
"""