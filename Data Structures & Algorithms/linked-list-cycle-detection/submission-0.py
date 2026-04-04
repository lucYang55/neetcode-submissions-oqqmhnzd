# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we need some kind of check to see if we have visited a node prev 
        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True 
        
        return False
