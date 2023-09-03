class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0
        counter = 0


        for num in nums:
            if counter == 0:
                result = num

            if num == result:
                counter += 1
            else:
                counter -= 1

        return result        