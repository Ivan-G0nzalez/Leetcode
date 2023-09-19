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
        
        result = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and romanNumber[s[i]] < romanNumber[s[i + 1]]:
                result -= romanNumber[s[i]]
            else:
                result += romanNumber[s[i]]
            
        return result