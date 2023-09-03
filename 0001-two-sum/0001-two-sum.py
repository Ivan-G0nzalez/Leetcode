class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i,num in enumerate(nums):
            objetive = target - num
            print(objetive)
            if objetive in result:
                return [ result[objetive], i]
            else:
                result[num] = i     

        return []        