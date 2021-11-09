"""
Write a function that takes in an array of unique integers and returns an
array of all permutations of those integers in no particular order.

input  = [1, 2, 3]
output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

"""


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
