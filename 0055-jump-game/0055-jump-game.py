class Solution:
    def jum(self, nums:List[int]):
        pass
    
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reacheable = 0
        
        for i in range(n):
            if reacheable < i:
                return False
            reacheable = max(reacheable, i+nums[i])  
        
        return True