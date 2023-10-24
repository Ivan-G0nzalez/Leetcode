/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isUnivalTree(root: TreeNode | null): boolean {
     if (!root){
        return true
        }

    if (!!root.right && root.val !== root.right.val){
        return false
    }

    if (!!root.left && root.val !== root.left.val){
         return false
     }

    return isUnivalTree(root.right) && isUnivalTree(root.left)
    
};