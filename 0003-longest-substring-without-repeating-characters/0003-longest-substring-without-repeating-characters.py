class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestComparation = ""
        longestResult = ""
        
        for letter in s:
            if len(longestResult) < len(longestComparation):
                    longestResult = longestComparation
            
            if letter not in longestComparation:
                longestComparation += letter
                
            else:
                longestComparation = longestComparation[longestComparation.index(letter) + 1:] + letter
                
                    
        return max(len(longestComparation), len(longestResult))                