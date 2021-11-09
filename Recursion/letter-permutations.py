"""

Given a list of unique letters, find all of its distinct permutations.

Input:

['a', 'b', 'c']

Output:

[['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c']
, ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]

"""
res = []


def backtracking(array, current):
    if len(current) == len(array):
        res.append(current)
        return
    for item in array:
        if item in current:
            continue
        backtracking(array, current + [item])


backtracking(['a', 'b', 'c'], res)
print(res)
