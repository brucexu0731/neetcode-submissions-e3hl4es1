# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def dfs(n, path_max):
            nonlocal res 
            if not n:
                return 
            
            if n.val >= path_max:
                res += 1
                dfs(n.left, n.val)
                dfs(n.right, n.val)
            else:
                dfs(n.left, path_max)
                dfs(n.right, path_max)
        
        dfs(root, -float('inf'))
        return res

        