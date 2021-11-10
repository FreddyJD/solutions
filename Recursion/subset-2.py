"""
Subsets II

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution 
in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""
def backtrack(nums, current, result):
    
    result.append(current)
    
    if(len(nums) == 0):
        return

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        backtrack(nums[i + 1:], current + [nums[i]], result)


# result = []
# backtrack(sorted(nums), [], result)
# return result