class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
            
        start_s = 0;
        start_t = 0;

        while start_t < len(t):
            if s[start_s] == t[start_t]:
                start_s += 1
            if start_s == len(s):
                return True
            start_t += 1        

        return False