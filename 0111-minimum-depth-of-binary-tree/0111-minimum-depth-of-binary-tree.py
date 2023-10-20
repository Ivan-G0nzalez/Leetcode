# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0
    

            left = dfs(root.left)
            right = dfs(root.right)

            if left == 0 or right == 0:
                return 1 + max(left, right)
            
            return 1 + min(left, right)

        return dfs(root)