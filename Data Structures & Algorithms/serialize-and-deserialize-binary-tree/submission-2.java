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

    String res = "";
    int i = 0;

    // Encodes a tree to a single string.
    // 12NN34NN5NN
    public String serialize(TreeNode root) {
        dfs(root);
        System.out.println(res.substring(0, res.length() - 1));
        return res.substring(0, res.length() - 1);
    }

    void dfs(TreeNode node){
        if (node == null){
            res += "N,";
            return;
        }
        res += node.val;
        res += ",";
        dfs(node.left);
        dfs(node.right);
    }



    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] arr = data.split(",");
        return dfs2(arr);
    }

    TreeNode dfs2(String[] arr){   
        if(arr[i].equals("N")){
            i++;
            return null;
        }

        TreeNode curr = new TreeNode(Integer.parseInt(arr[i]));
        i++;
        curr.left = dfs2(arr);
        curr.right = dfs2(arr);

        return curr;
    }
}
