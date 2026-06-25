# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        answer=[]
        queue=deque()
        queue.append(root)
        while queue:
            nest=[]
            
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                nest.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(nest)
        return answer

