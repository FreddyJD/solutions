class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0 for _ in range(n)] 
        dp[0] = 1 
        dp[1] = 2 
        
        for climb in range(2, n):
            dp[climb] = dp[climb - 1] + dp[climb - 2]
        
        return dp[-1]