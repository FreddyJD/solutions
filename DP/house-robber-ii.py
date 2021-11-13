def rob(nums):
    if len(nums) <= 2:
        return max(nums)

    return max(rob_segment(nums[1:]), rob_segment(nums[:-1]))


def rob_segment(houses):
    dp = [0 for _ in range(len(houses))]
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for index in range(2, len(houses)):
        dp[index] = max(dp[index - 2] + houses[index], dp[index - 1])
    return max(dp[-1], dp[-2])
