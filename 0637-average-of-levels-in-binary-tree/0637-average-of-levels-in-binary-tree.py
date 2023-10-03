# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        
        self.levelAverage(root, result)
        
        return result
    
    def levelAverage(self, node, result):
        if not node:
            return
        
        level_sum = 0
        level_count = 0
        
        # Utiliza una cola para realizar un recorrido por niveles (BFS)
        queue = [node]
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)
                level_sum += current.val
                level_count += 1
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            # Calcula el promedio del nivel y agrega al resultado
            result.append(float(level_sum) / level_count)
            
            # Reinicia las variables para el próximo nivel
            level_sum = 0
            level_count = 0