from typing import Counter

response = []
def backtrack(current, numbers_counter):
    if len(current) == len(nums):
        response.append(current[:])
        return

    for num in numbers_counter:
        if numbers_counter[num] > 0:
            numbers_counter[num] =- 1
            backtrack(current + [num], numbers_counter)
            numbers_counter[num] =+ 1

backtrack([], Counter(nums))
print(response)
