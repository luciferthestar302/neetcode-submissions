# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head

        while n>0:
            right = right.next
            n-=1
        
        #STEP2: moving both left and right pointers together, before that right hits null
        while right:
            left = left.next
            right = right.next
        
    #Removing the nth node - by skipping it
        left.next = left.next.next
        return dummy.next
#Time - O(n), Space - O(1)

        