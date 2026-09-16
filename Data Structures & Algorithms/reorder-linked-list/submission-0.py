# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        current = second
        while current != None:
            next_val = current.next
            current.next = prev
            prev = current
            current = next_val
        second = prev
        first = head
        while second is not None: 
            next_first_val = first.next
            next_second_val = second.next

            first.next = second
            second.next = next_first_val

            first = next_first_val
            second = next_second_val
