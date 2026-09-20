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

public class Codec {

    StringBuilder res;
    int i = 0;
    String[] arr;

    // Encodes a tree to a single string.
    // 12NN34NN5NN
    public String serialize(TreeNode root) {
        res = new StringBuilder();
        dfs(root);
        res.setLength(res.length() - 1);
        //System.out.println(res.substring(0, res.length() - 1));
        return res.toString();
    }

    void dfs(TreeNode node){
        if (node == null){
            res.append("N,");
            return;
        }
        res.append(node.val).append(",");
        dfs(node.left);
        dfs(node.right);
    }



    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        arr = data.split(",");
        return dfs2();
    }

    TreeNode dfs2(){   
        if(arr[i].equals("N")){
            i++;
            return null;
        }

        TreeNode curr = new TreeNode(Integer.parseInt(arr[i]));
        i++;
        curr.left = dfs2();
        curr.right = dfs2();

        return curr;
    }
}
