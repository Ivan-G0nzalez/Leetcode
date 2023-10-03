class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        
        
        for index in range(len(s)):
            count_s[s[index]] = 1 + count_s.get(s[index], 0)
            count_t[t[index]] = 1 + count_t.get(t[index], 0)
        
        for counter in count_s:
            if count_s[counter] != count_t.get(counter, 0):
                return False
        
        return True