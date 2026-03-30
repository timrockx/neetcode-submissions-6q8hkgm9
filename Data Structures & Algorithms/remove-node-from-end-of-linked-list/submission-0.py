# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # iterate to find length

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        index = length - n

        if index == 0:
            return head.next

        curr = head
        for i in range(length-1):
            if i == index-1:
                # we can do this bc if we remove 2nd to last, then it should be None anyways
                curr.next = curr.next.next
                break
            curr = curr.next                
        
        return head

        