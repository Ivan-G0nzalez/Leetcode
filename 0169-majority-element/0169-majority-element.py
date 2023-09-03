class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for num in set(nums):
            counter = nums.count(num)
            if counter > (len(nums) / 2):
                return num