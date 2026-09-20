/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {

        return dfs(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        
    }

    boolean dfs (TreeNode node, int minLeft, int maxRight) {
        if (node == null) {
            return true;
        }

        if (node.left != null){
            if (node.left.val >= node.val || 
            node.left.val <= minLeft ||
            !dfs(node.left, minLeft, Math.min(maxRight, node.val))){
                return false;
            }
        }
        if (node.right != null){
            if (node.right.val <= node.val || 
            node.right.val >= maxRight ||
            !dfs(node.right, Math.max(node.val, minLeft), maxRight)){
                return false;
            }
        }

        return true;
    }
}
