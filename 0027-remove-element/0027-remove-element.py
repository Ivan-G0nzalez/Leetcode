class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        
        for i, num in enumerate(nums):
            if num != val:
                nums[index] = nums[i]
                index += 1
        
        return index