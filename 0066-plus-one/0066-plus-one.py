class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        result = ""

        for num in digits:
            result += str(num)

        return [int(num) for num in list(str(int(result) + 1))]
    