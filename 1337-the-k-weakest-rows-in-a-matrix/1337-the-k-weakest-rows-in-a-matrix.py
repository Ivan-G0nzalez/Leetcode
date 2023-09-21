class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
    
        for index,row in enumerate(mat):
            soldier = (sum(row) ,index)
            result.append(soldier)

        result.sort()     

        return [index for _,index in result[:k]]