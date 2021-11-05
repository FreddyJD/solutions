# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, node): 
        if node.next is None: 
            return node
        else:
            new_linked_list = self.reverse_linked_list(node.next)
            node.next.next = node
            node.next = None
            return new_linked_list
            
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        return self.reverse_linked_list(head)