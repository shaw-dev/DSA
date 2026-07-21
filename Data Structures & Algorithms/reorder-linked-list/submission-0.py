# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next :
            return None


        slow = head
        fast = head
#divided
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next= None
# reverse
        prev = None
        curr = sec
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        sec = prev
        first = head

        while sec:
            temp1 = first.next
            temp2 = sec.next

            first.next= sec
            sec.next = temp1
            first=temp1
            sec=temp2
        