class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            elif i - hashmap[nums[i]] <= k:
                return True
            else:
                hashmap[nums[i]] = i
        
        return False