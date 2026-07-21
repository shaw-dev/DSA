"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        
        curr = head
        maps = {None: None}

       
        while curr:
            temp = curr.val
            maps[curr] = Node(temp)

            
            curr=curr.next
        
        curr = head
        while curr:
            temp = maps[curr]
            temp.next = maps[curr.next]
            temp.random = maps[curr.random]

            curr = curr.next
        return maps[head]




