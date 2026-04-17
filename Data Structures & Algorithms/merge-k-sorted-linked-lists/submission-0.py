# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []
        for ll in lists:

            while ll:
                heapq.heappush(min_heap, ll.val)
                ll = ll.next

        print(min_heap)

        curr = head = ListNode()
        while min_heap:
            curr.next = ListNode(heapq.heappop(min_heap))
            curr = curr.next

        return head.next