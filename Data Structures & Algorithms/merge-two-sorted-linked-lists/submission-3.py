# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #we create a dummy node having data value 0 as a starting point
        curr = dummy #curr is the moving pointer initally pointing where dummy is pointing.
        while list1 and list2: #validating that both lists are non-empty
            if list1.val<list2.val:
                curr.next = list1
                list1 = list1.next #moving to the next node of list1
            else:
                curr.next = list2
                list2 = list2.next #moving to the next node of list 2

            curr = curr.next #moving curr pointer to next of the node(this node will be decided from the above if else condition)
        
        if list1:    #if list 1 is non-empty
            curr.next = list1
        else:        #if list 2 is non-empty
            curr.next = list2
        return dummy.next

        