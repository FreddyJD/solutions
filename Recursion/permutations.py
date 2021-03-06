"""
Write answer function that takes in an array of unique integers and returns an
array of all permutations of those integers in no particular order.

input  = [1, 2, 3]
output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

"""


"""

First brute-force solution

"""




import functools
def get_permutations(array):
    permutations = []
    build_permutations(array, [], permutations)
    return permutations


def build_permutations(array, current, permutations):
    if not len(array) and len(current):
        permutations.append(current)
    else:
        for num_index in range(len(array)):
            new_array = array[:num_index] + array[num_index + 1:]
            new_current = current + [array[num_index]]
            build_permutations(new_array, new_current, permutations)


"""

With generators


"""


def permutations_gen(nums):
    answers = [[]]
    for num in nums:
        new_answers = []
        for answer in answers:
            for i in range(len(answer) + 1):
                res = answer[:i] + [num] + answer[i:]
                new_answers.append(res)
                if len(res) == 3:
                    yield res
        answers = new_answers
    return answers


for num in permutations_gen([10, 20, 30]):
    print(num)


"""

My favorite solution 

"""


def permutations(array, current, result):
    if len(current) == len(array):
        result.append(current)
        return

    for num in array:
        if num in current:
            continue
        permutations(array, current + [num], result)


# results = []
# permutations([1, 2, 3], [], results)
# print(results)


"""
@permutations2

time complexity
the algo perform at O(n * m!) 
n = is our numbers array that we have to move through 
m = are our the partial permutations we have to do with out bruteforce/backtrack method

space complexity
O(m!) 
m = is the amount of solutions we have to keep in our stack 
"""

# enhancement with sets
def _permutations(array, current, result):
    print(current)
    if len(current) == len(array):
        result.append(list(current))
        return

    for num in array:
        if num not in current:
            current.add(num)
            _permutations(array, current, result)
            current.remove(num)

res = []
_permutations({1, 2, 3}, set(), res)
# _permutations([1, 2, 3], [], res)
print(res)
