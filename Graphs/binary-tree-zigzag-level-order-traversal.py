"""
Time Complexity: O(n)

We traverse every edge and node once but since the number of
edges is n - 1, then this simply becomes O(n).
"""
from collections import deque

def bfs(root):
    if root is None:
        return

    reverse_order = False
    queue = deque([root])

    while queue:
        length_queue = len(queue)
        temp = []
        for _ in range(length_queue):
            node = queue.popleft()
            temp.append(node.val)
            for child_node in [node.left, node.right]:
                if child_node is not None:
                    queue.append(child_node)
        if reverse_order:
            reverse_order = False
            temp.reverse()
            yield temp
        else:
            reverse_order = True
            yield temp

# return list(bfs(root))
