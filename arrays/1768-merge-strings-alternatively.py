class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        len1, len2 = len(word1), len(word2)
        max_chars = max(len1, len2)
        
        word = ""

        for i in range(max_chars):
            if i < len1:
                word = word + word1[i]
            if i < len2:
                word = word + word2[i]
        
        return word