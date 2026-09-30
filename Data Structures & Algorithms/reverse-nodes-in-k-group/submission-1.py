# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        -given a linkedlist reverse first k elements, and elements after
        -we can probably do more of a brute force type of approach
            -we turn the head into a list
            -from there we can slice and reverse the elements in the list
            -afterwards, we do the same and try to reverse the elements after the first k eles
            -then we turn it back into a linked list

        """
        curr = head
        data = []
        data_lists = []
        reverse_data_lists = []
        while curr != None:
            data.append(curr.val)
            curr = curr.next
        for i in range(0, len(data), k):
            data_lists.append(data[i:i + k])
        for data_list_ind in range(len(data_lists)):
            if len(data_lists[data_list_ind]) >= k:
                data_lists[data_list_ind].reverse()
        clean_data = []
        for each_list in data_lists:
            for element in each_list:
                clean_data.append(element)
        new_curr = ListNode(None)
        dummy = new_curr
        for element in clean_data:
            dummy.next = ListNode(element)
            dummy = dummy.next
        return new_curr.next

         