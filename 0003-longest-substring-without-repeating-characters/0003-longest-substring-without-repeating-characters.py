class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        currentValue = ""
        comparationValue = ""
        
        for letter in s:
            
            if len(currentValue) > len(comparationValue):
                comparationValue = currentValue
        
            if letter not in currentValue:
                currentValue += letter
            else:
                currentValue = currentValue[currentValue.index(letter)+ 1:] + letter
            
            
       
        return max(len(currentValue), len(comparationValue))