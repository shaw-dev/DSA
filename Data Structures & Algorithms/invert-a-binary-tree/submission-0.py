# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root ==None:
            return None
        
        answer =[root]

        while answer:
            node = answer.pop()
            node.left,node.right=node.right,node.left
        

            if node.left:
                answer.append(node.left)
            if node.right:
                answer.append(node.right)
        return root

        