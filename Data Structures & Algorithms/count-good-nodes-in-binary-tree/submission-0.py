# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.answer=0

        def dfs(node,maxsofar):
            if not node:
                return 

            if node.val>=maxsofar:
                self.answer += 1
            maxsofar=max(maxsofar,node.val)

            dfs(node.left,maxsofar)
            dfs(node.right,maxsofar)
        dfs(root,root.val)
        return self.answer

            

        