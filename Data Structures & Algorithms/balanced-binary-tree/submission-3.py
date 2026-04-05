# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            dl = 1 + dfs(node.left)
            dr = 1 + dfs(node.right)

            if dl - dr > 1 or dr - dl > 1:
                balanced = False
            
            return max(dl, dr)
        
        dfs(root)

        return balanced


            

 
        
            
            



            