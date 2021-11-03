class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        t1 = len(text1)
        t2 = len(text2)
        dpMatrix = [[0 for _ in range(t2 + 1)] for _ in range(t1 + 1)]
        response = 0

        for i in range(1, t1 + 1):
            for j in range(1, t2 + 1):
                if text1[i-1] == text2[j-1]:
                    dpMatrix[i][j] = dpMatrix[i - 1][j - 1] + 1
                    response = max(dpMatrix[i][j], response)
                else:
                    dpMatrix[i][j] = max(dpMatrix[i - 1][j] , dpMatrix[i][j - 1])

        return dpMatrix[-1][-1]