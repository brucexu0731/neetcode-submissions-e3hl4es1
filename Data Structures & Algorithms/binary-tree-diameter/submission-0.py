# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(n):
            nonlocal res
            if not n:
                return 0
            
            left, right = 0, 0

            if n.left:
                left = dfs(n.left)
            
            if n.right:
                right = dfs(n.right)

            res = max(left + right, res)

            return 1 + max(left, right)
        
        dfs(root)
        return res
        