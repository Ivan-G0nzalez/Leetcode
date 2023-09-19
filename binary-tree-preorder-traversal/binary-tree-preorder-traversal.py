# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        result = []
        
        result.append(root.val)
        
        left_result = self.preorderTraversal(root.left)
        
        result.extend(left_result)
        
        right_result = self.preorderTraversal(root.right)
        
        result.extend(right_result)
        
        return result