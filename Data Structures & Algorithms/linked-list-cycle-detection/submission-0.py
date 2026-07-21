# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        visited=set() #value: index

        while head:
            if head in visited:
                return True
            elif head not in visited:

                visited.add(head)
                head = head.next
        
        return False


            