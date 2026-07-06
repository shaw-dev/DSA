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
        q=deque()
        q.append(root)
        while q:
            nested =[]
            l = len(q)
            for i in range(l):
                pop = q.popleft()
                nested.append(pop.val)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            answer.append(nested)
        return answer
        