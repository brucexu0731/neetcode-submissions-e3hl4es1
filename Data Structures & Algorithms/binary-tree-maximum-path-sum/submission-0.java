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

// class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;
//     TreeNode(){}
//     TreeNode(int val){this.val = val;}
//     TreeNode(int val, TreeNode left, TreeNode right){
//         ...
//     }
// }

class Solution {
    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return maxSum;
        
    }

    int dfs(TreeNode node){
        if (node == null){
            return 0;
        }

        int maxLeft = Math.max(dfs(node.left), 0);
        int maxRight = Math.max(dfs(node.right), 0);

        maxSum = Math.max(maxSum, node.val + maxLeft + maxRight);

        return node.val + Math.max(maxLeft, maxRight);
    }
}
