from collections import deque

"""
Shortest path A to B with BFS

Time Complexity: O(n+m)

we adopt the convention that n denote the number of nodes in the graph 
and m the numebr of edges. The time spent is equal to the number of nodes 
and edges in the worst case. Consider for example a linear graph 0->1->2->3 
and so on where we want to get from end to end, we would traverse every 
node and edge exactly once.



"""


def shortest_path_two_nodes(graph, a, b):
    def get_neighbors(node):
        return graph[node]

    def bfs(root, target):
        level = 0
        queue = deque([root])
        visited = set([root])
        while len(queue) > 0:
            n = len(queue)
            for n in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                for neighbor in get_neighbors(node):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            level += 1
    return bfs(a, b)


# testing
_graph = {
    1: [2],
    2: [3, 1],
    3: [2, 5],
    5: []
}

print(shortest_path_two_nodes(_graph, 1, 5))
