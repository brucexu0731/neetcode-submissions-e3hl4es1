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
    boolean found = false; 

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> path1 = new ArrayList<>();
        List<TreeNode> path2 = new ArrayList<>();
        dfs(root, path1, p);
        found = false;
        dfs(root, path2, q);

        for (int i = Math.min(path1.size(), path2.size()) - 1; i >= 0; i --){
            if (path1.get(i) == path2.get(i)){
                return path1.get(i);
            }
        }

        return null;
    }

    private void dfs(TreeNode node, List<TreeNode> path, TreeNode target) {
        if (found) {
            return;
        }

        if (node == null) {
            return;
        }

        path.add(node);
        if (node == target) {
            found = true;
            return;
        }

        dfs(node.left, path, target);
        dfs(node.right, path, target);
        if (found) {
            return;
        }
        path.remove(path.size() - 1);
    }
}
