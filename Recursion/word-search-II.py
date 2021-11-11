"""
# Solution Research
For the question we need to use two of the patterns we have learned - DFS and Trie 
Firstly, we want to know whether or not we have correctly made a word. For this we 
first insert all the possible words into a trie.

As we dfs through the grid to make the possibilities we move down the trie at the 
same time. Once we reach a point where the next character does not exist in that 
particular node's child in the trie then we know no word in our list of words matches 
that sequence of characters. We therefore do not search any more cells in the grid 
as we know that no children contain that particular word. We also make sure to 
carefully mark which nodes in the trie we have reached.

We then repeat this process for every cell in the grid to check if it is possible 
to make a word. By the end we query every word in our trie to figure out which words
we can make. Another minor implementation detail is that we need to make sure not 
to go back on cells we have visited. Therefore, we need to maintain a visited array 
that keeps marks cells that we reached and we unmark cells that we have not visited. 
It can also be noted that the character a has an ascii code of 97.

"""
from typing import List

def insert(trie_pos: int, s: str, str_pos: int, trie: List[List[int]], sz: int):
    # the array implementation is a 2-d matrix where every column is a new trie node
    # we can therefore create our trie by pointing to the next node in the trie in the appropriate column
    if str_pos == len(s):
        return sz
    trie_char = ord(s[str_pos]) - 97
    if trie[trie_char][trie_pos] == 0:
        trie[trie_char][trie_pos] = sz
        sz += 1
    return insert(trie[trie_char][trie_pos], s, str_pos + 1, trie, sz)


def query(trie_pos: int, s: str, str_pos: int, trie: List[List[int]], reached: List[bool]) -> bool:
    # make sure to check we have moved through the entire word as well as the fact that we have gone through this path
    if not reached[trie_pos]:
        return False
    if str_pos == len(s):
        return True
    trie_char = ord(s[str_pos]) - 97
    return query(trie[trie_char][trie_pos], s, str_pos + 1, trie, reached)


def dfs(i: int, j: int, idx: int, matrix: List[str], trie: List[List[int]], reached: List[bool], vis: List[List[bool]]):
    n, m = len(matrix), len(matrix[0])
    # marks our trie to say we can make this particular prefix in our trie
    reached[idx] = True
    # the vis array keeps track of the cells we have visited we mark it once we move through and unmark when we leave
    # this is because we don't want our current path to loop back on itself but once we move up the recursive stack we have no longer visited this cell and we need to unmark it for other paths moving through this cell
    vis[i][j] = True
    if i + 1 < n and not vis[i + 1][j] and trie[ord(matrix[i + 1][j]) - 97][idx] != 0:
        dfs(i + 1, j, trie[ord(matrix[i + 1][j]) - 97]
            [idx], matrix, trie, reached, vis)

    if i - 1 >= 0 and not vis[i - 1][j] and trie[ord(matrix[i - 1][j]) - 97][idx] != 0:
        dfs(i - 1, j, trie[ord(matrix[i - 1][j]) - 97]
            [idx], matrix, trie, reached, vis)

    if j + 1 < m and not vis[i][j + 1] and trie[ord(matrix[i][j + 1]) - 97][idx] != 0:
        dfs(i, j + 1, trie[ord(matrix[i][j + 1]) - 97]
            [idx], matrix, trie, reached, vis)

    if j - 1 >= 0 and not vis[i][j - 1] and trie[ord(matrix[i][j - 1]) - 97][idx] != 0:
        dfs(i, j - 1, trie[ord(matrix[i][j - 1]) - 97]
            [idx], matrix, trie, reached, vis)

    vis[i][j] = False


def word_search_ii(matrix: List[str], words: List[str]) -> List[str]:
    # note that when setting the arrays we only need to pick sufficiently high values.
    # size of the matrix is given but trie is a bit hard to predict.
    # sometimes a good technique can be to arbtrarily increase the sizes of the array until we pass the tests!
    sz = 1
    # here we show an alternative implementation of a trie using an array or list, use whatever implementation you most prefer
    trie = []
    reached = [False] * 300001
    vis = []
    # initialize lists
    for i in range(100):
        vis.append([])
    for i in range(100):
        for j in range(100):
            vis[i].append(False)
    for i in range(26):
        trie.append([])
    for i in range(26):
        for j in range(300001):
            trie[i].append(0)
    # insert all words into our trie
    for word in words:
        sz = insert(0, word, 0, trie, sz)
    # we loop through our matrix and choose every cell as a potential starting point for our path
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trie_idx = trie[ord(matrix[i][j]) - 97][0]
            if trie_idx > 0:
                dfs(i, j, trie_idx, matrix, trie, reached, vis)
    reached[0] = True
    ans = []
    for word in words:
        if query(0, word, 0, trie, reached):
            ans.append(word)
    return ans
