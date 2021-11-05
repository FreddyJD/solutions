# https://leetcode.com/problems/reverse-string/

"""
Recursion
"""
class Solution:
    def reverse_string(self, s, left, right): 
        if left < right: 
            s[left], s[right] = s[right], s[left]
            self.reverse_string(s, left + 1, right - 1)
        return s
        
    def reverseString(self, s) -> None:
        return self.reverse_string(s, 0, len(s) - 1)


"""
Generators
"""

def reverse_string(s):
    for char in range(len(s) - 1, -1, -1): 
        yield s[char]
    return

test_string = "hello world"
print(list(reverse_string(test_string)))