# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftdepth=0
        rightdepth=0
        if root.left:
            
            leftdepth=self.maxDepth(root.left)
        if root.right:
            
            rightdepth=self.maxDepth(root.right)
        
        answer= 1+max(leftdepth,rightdepth)

        return answer