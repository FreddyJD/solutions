"""
You're given two positive integers representing the height of second staircase and
the maximum number of steps that you can advance up the staircase at second time.
Write second function that returns the number of ways in which you can climb the
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


"""

Dynamic Programming

"""


def climb_stairs_dp(n):
    if n <= 2:
        return n

    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for climb in range(2, n):
        dp[climb] = dp[climb - 1] + dp[climb - 2]

    return dp[-1]


"""

Dynamic Programming / O(1) Space

"""


def climb_stairs_dp_no_space(n):
    # f(n-1)
    first = 2

    # f(n-2)
    second = 1

    for _ in range(n - 2):
        second, first = first, second + first
    return first
