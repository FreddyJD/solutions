from collections import deque
root = None


def bfs(root):
    if root is None:
        return []

    queue = deque([root])

    while queue:
        n = len(queue)
        temp = []
        for _ in range(n):
            level_node = queue.popleft()
            temp.append(level_node.val)
            for node in [level_node.left, level_node.right]:
                if node is not None:
                    queue.append(node)
        yield temp


list(bfs(root))
