class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(candidates_current, candidate_index, combination_sum):
            if combination_sum == target:
                candidate_combination_copy = candidates_current.copy()
                return res.append(candidate_combination_copy)
            if combination_sum > target or candidate_index >= len(candidates): 
                return
            candidates_current.append(candidates[candidate_index])
            current_sum = candidates[candidate_index] + combination_sum
            dfs(candidates_current, candidate_index, current_sum)
            candidates_current.pop()
            dfs(candidates_current, candidate_index + 1, combination_sum)
        
        dfs([], 0, 0)
        return res
