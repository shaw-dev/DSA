# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        # Is the current tree exactly the same as subRoot?
        if self.dfs(root, subRoot):
            return True

        # Otherwise search the left or right subtree
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
        if not root and not subRoot:
            return True

        # One empty, one not -> different
        if not root or not subRoot:
            return False

        # Values don't match
        if root.val != subRoot.val:
            return False

        # Check left and right children
        return (
            self.dfs(root.left, subRoot.left) and
            self.dfs(root.right, subRoot.right)
        )
        
            
        
        