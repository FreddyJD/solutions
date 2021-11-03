class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.rob_segment(nums[1:]), self.rob_segment(nums[:-1]))
        
    def rob_segment(self, houses):
        dp = [0 for _ in range(len(houses))]
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for house_index in range(2, len(houses)): 
            dp[house_index] = max(dp[house_index - 2] + houses[house_index], dp[house_index - 1])
        return max(dp[-1], dp[-2])        