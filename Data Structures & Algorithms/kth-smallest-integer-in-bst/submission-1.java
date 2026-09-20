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

    int target;
    int counter = 0;

    public int kthSmallest(TreeNode root, int k) {
        dfs(root, k);
        return target;
        
    }

    void dfs(TreeNode node, int k){
        if (node == null) {
            return;
        }

        dfs(node.left, k);
        if (counter > k) {
            return;
        }
        counter += 1;
        if (counter == k){
            target = node.val;
        }
        dfs(node.right, k);

    }
}
