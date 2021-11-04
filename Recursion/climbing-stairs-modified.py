"""
You're given two positive integers representing the height of a staircase and
the maximum number of steps that you can advance up the staircase at a time.
Write a function that returns the number of ways in which you can climb the
staircase.

input = height = 4 | maxSteps = 2
output = 5

"""
def staircase_traversal(height, max_steps):
    if height <= 1:
        return 1
    steps = 0
    for step in range(1, min(max_steps, height) + 1):
        steps += staircase_traversal(height - step, max_steps)
    return steps