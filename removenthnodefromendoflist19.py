# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #find the node right before the delete
        #skip over that node

        #since we do not know the size of the nodes, we have to track it using another set of nodes
        dummy = ListNode(0,head) #added the extra node to get the node one before the removal
        left = dummy
        right = head

        while n > 0: #get nth node of head
            right = right.next
            n -= 1 #counter

        #right made n jumps, or (n+1)th node of head
        #whatever the remaining of right nodes, will be the count we need to get to nth from end
        while right: #right is shorter
            left = left.next
            right = right.next
        #left should've performed [len(head)-(n)+ (1 for None)] jumps
        
        left.next = left.next.next #skip over the mode
        return dummy.next #return the next since the first node was a dummy
        

        
            