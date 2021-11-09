# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int):
        cache = {}

        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in cache:
                return cache[n]

            response = []
            for left_tree in range(n):
                right_tree = n - 1 - left_tree
                left, right = backtrack(left_tree), backtrack(right_tree)

                for left_node in left:
                    for right_node in right:
                        response.append(TreeNode(0, left_node, right_node))

            cache[n] = response
            return response

        return backtrack(n)
