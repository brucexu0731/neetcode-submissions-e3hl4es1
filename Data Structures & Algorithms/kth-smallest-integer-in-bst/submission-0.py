# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val 
        
        def dfs(node, cnt):  
            nonlocal res 
            if node == None:
                return cnt
            
            cnt = dfs(node.left, cnt)
            cnt -= 1
            if cnt == 0:
                res = node.val 
            cnt = dfs(node.right, cnt)

            return cnt
        
        dfs(root, k)
        return res