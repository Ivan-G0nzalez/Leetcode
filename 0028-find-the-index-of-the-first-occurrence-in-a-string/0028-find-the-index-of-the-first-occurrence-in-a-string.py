class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        text_len = len(haystack)
        substring_len = len(needle)

        for i in range((text_len - substring_len) + 1):
            if haystack[i: i + substring_len] == needle:
                return i

        return -1