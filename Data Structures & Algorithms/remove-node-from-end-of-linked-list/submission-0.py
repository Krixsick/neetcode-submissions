# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_len = head
        head_len = 0
        while curr_len != None:
            head_len += 1
            curr_len = curr_len.next

        curr = head
        index = head_len - n
        if index == 0:
            return head.next
        for i in range(index):
            if i + 1 == index:
                tmp = curr.next
                # print(tmp.val)
                curr.next = tmp.next
                break
            curr = curr.next
            print(curr.val)
        return head
        """
            -we remove nth node from end of list
            -so n = 2 -> second last, n = 1 -> last, etc
            -brute force sol:
                - wouldn't we just keep looping and do like index = len(head) - n, would give us the index of which value we should remove
                -from that index we would just do the prev_value = to curr.next
                -edge case: what if there's one element and we remove that? 
        """