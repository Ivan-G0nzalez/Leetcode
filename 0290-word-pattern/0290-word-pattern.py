class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
    
        if len(words) != len(pattern): 
            return False

        word_map = {}
        char_map = {}


        for word,char in zip(words, pattern):
            if word not in word_map and char not in char_map:
                word_map[word] = char
                char_map[char] = word

            elif word != char_map.get(char) or char != word_map.get(word):
                return False

        return True