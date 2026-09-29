# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = []
        for i in range(len(lists)):
            head = lists[i]
            while head != None:
                data.append(head.val)
                head = head.next
        data = sorted(data)
        curr = ListNode(None)
        head = curr
        for element in data:
            head.next = ListNode(element)
            head = head.next
        return curr.next
    