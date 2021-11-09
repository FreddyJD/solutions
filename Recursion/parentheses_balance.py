"""
Usign yields
"""


def parentheses_balance(n):
    if n == 0:
        yield ""
        return
    # 2
    for i in range(n):
        for y in parentheses_balance(i):
            for z in parentheses_balance(n - i - 1):
                yield '(' + y + ')' + z


"""

My solution with backtracking

"""


def parentheses_backtrack(n, start, end, string, results):
    if len(string) == 2 * n:
        results.append(string)

    if start < n:
        parentheses_backtrack(n, start + 1, end, string + "(", results)

    if start > end:
        parentheses_backtrack(n, start, end + 1, string + ")", results)


results = []
parentheses_backtrack(3, 0, 0, "", results)
print(results)


"""

DP way.
(Top-down implementation)

Stole it from leetcode, but seems really OP for the problem itself.
https://leetcode.com/problems/generate-parentheses/discuss/446245/Python3-Backtracking-and-DP



"""


def generateParenthesis(n):
    # @lru_cache(None)
    def fn(k):
        """Return k pairs of parentheses"""
        if k == 0:
            return [""]
        ans = []
        for i in range(k):
            ans.extend([f'({x}){y}' for x in fn(k-i-1) for y in fn(i)])
        return ans

    return fn(n)
