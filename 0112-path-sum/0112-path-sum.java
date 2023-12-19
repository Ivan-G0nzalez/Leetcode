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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null){
            return false;
        }
        
        
        int subSum = targetSum - root.val;
        
        if (subSum == 0 && root.left == null && root.right == null){
            return true;
        }
        
        boolean ans = false;
        
        if (root.left != null){
            ans = ans || hasPathSum(root.left, subSum);
        }
        
        if (root.right != null){
            ans = ans || hasPathSum(root.right, subSum);
        }
            
        return ans;
    }
}