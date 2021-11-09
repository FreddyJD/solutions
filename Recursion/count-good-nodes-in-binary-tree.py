# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, prior_value):
    if node is None:
        return 0

    good_nodes = 0

    if prior_value <= node.val:
        good_nodes += 1

    good_nodes += dfs(node.left, max(prior_value, node.val))
    good_nodes += dfs(node.right, max(prior_value, node.val))

    return good_nodes


def good_nodes(root):
    # Test sends negative numbers
    return dfs(root, float('-inf'))
