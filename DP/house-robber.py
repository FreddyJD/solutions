def rob(nums):
    if len(nums) < 2:
        return max(nums)

    cache = [0 for _ in range(len(nums))]
    cache[0] = nums[0]
    cache[1] = max(nums[0], nums[1])

    for index in range(2, len(nums)):
        cache[index] = max(cache[index - 2] + nums[index], cache[index - 1])

    return max(cache[-1], cache[-2])
