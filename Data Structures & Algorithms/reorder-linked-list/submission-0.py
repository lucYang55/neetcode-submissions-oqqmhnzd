# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        dummy = ListNode()
        tail = dummy

        # split into two halves
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        shalf = slow.next
        prev = slow.next = None

        while shalf != None:
            temp = shalf.next
            shalf.next = prev
            prev = shalf
            shalf = temp

        first = head
        shalf = prev

        while shalf:
            tmp1, tmp2 = first.next, shalf.next
            first.next = shalf
            shalf.next = tmp1
            first = tmp1
            shalf = tmp2

