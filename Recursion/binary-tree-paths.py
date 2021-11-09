
def dfs(node, current_path, response):
    if node:
        current_path = current_path + [str(node.val)]
        if not node.left and not node.right:
            path = "->".join(current_path)
            response.append(path)
            return
        else:
            dfs(node.left, current_path, response)
            dfs(node.right, current_path, response)


def binaryTreePaths(root):
    response = []
    dfs(root, [], response)
    return response
