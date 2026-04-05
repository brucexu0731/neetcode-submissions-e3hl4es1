# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        if index == 0 and index == len(preorder) - 1:
            root.left = None
            root.right = None 
        elif index == 0:
            root.left = None 
            root.right = self.buildTree(preorder[index + 1:], inorder[index + 1 :])
        elif index == len(preorder) - 1:
            root.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
            root.right = None
        else:
            root.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
            root.right = self.buildTree(preorder[index + 1:], inorder[index + 1 :])
        return root