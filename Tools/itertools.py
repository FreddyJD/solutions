
import itertools

"""
@cycle
"""
_list = ['a', 'b', 'c']

# defining iterator
iterators = itertools.cycle(_list)

# for in loop
for i in range(6):
    # Using next function
    print(next(iterators), end=" ")

"""
@product
"""

print("The cartesian product using repeat:")
print(list(itertools.product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(itertools.product(['yo', 'do', 'so'], '2')))
print()

print("The cartesian product of the containers:")
t3 = itertools.product('AB', [3, 4])
print(list(t3))


"""
@permutations
"""

print("All the permutations of the given list is:")
print(list(itertools.permutations([1, 'aa'], 2)))
print()

print("All the permutations of the given string is:")
print(list(itertools.permutations('AB')))

print("All the permutations of the given container is:")
print(list(itertools.permutations(range(3), 2)))


"""
@chain
"""


# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# using chain() to print all elements of lists
print("All values in mentioned chain are : ")
print(list(itertools.chain(li1, li2, li3)))


"""
@islice
"""

# initializing list
li = [2, 4, 5, 7, 8, 10, 20]

# using islice() to slice the list acc
print("The sliced list values are : ")
print(list(itertools.islice(li, 1, 6, 2)))


"""
@permutations
"""


a = "tST"

# no length entered so default length
p = itertools.permutations(a)

# Print the obtained permutations
for j in list(p):
    print(j)
