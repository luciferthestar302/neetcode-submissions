# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #point to last node of the list
        curr = head #points to node 0
        
        while curr is not None:
            temp = curr.next #initially curr.next is the next pointer having address stored of node 1 which is moved to temp
            curr.next = prev #now curr.next this pointer of first node (node 0) will point to NULL(prev) which depicts this is the last node
            prev = curr #now prev pointer will move to curr which is first node(node 0)
            curr = temp  #curr moves to second node which is node 1
        return prev #As prev pointer will become new head pointer
