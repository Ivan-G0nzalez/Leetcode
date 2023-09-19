class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanNumber = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        start = 0
        end = len(s)
        
        result = 0
        
        while start < end:
            if start < len(s) - 1 and romanNumber[s[start]] < romanNumber[s[start + 1]]:
                result -= romanNumber[s[start]]
            else: 
                result += romanNumber[s[start]]
            
            start += 1
        
        return result