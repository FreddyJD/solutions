def dfs(node):
    if node is None:
        return 0

    left_node = dfs(node.left)
    right_node = dfs(node.right)

    if left_node is None or right_node is None:
        return None

    if abs(left_node - right_node) > 1:
        return None

    return max(right_node, left_node) + 1


def is_balanced(tree):
    return dfs(tree) is not None
