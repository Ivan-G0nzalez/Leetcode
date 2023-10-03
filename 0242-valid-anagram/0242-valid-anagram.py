class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        if len(s) != len(t):
            return False
        
        letter_s = self.getLetter(s)
        letter_t = self.getLetter(t)
        
        for letter in letter_s:
            if letter not in letter_t or letter_s[letter] != letter_t[letter]:
                return False
        
        return True
        
    
    def getLetter(self, word):
        letters = {}
        for letter in word:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        return letters
            