class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i in range(len(nums)):
            current = nums[i]
            if current in hashmap and i - hashmap[current] <= k:
                return True
            else:
                hashmap[current] = i
                
        
        return False