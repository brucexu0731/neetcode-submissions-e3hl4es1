# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True
        def height(root):
            nonlocal balanced 
            if not root:
                return 0
            
            hl = height(root.left)
            hr = height(root.right)
            
            if hl - hr > 1 or hr - hl > 1:
                balanced = False
            
            hroot = 1 + max(hl, hr)

            return hroot
        
        height(root)
        return balanced



            

 
        
            
            



            