class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        
        cache = [0 for _ in range(len(nums))]
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        
        for house_index in range(2, len(nums)):
            cache[house_index] = max(cache[house_index - 2] + nums[house_index], cache[house_index - 1])
        
        return max(cache[-1], cache[-2])