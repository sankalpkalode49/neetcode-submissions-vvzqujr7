class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_w = ""
        i = 0
        j = 0
        if len(word1) >= len(word2):
            while j < len(word2):
                new_w = new_w + word1[i]
                new_w = new_w + word2[j]
                i +=1
                j +=1
            new_w = new_w + word1[i:]
            return new_w
        else:
            while i < len(word1):
                new_w = new_w + word1[i]
                new_w = new_w + word2[j]
                i +=1
                j +=1
            new_w = new_w + word2[j:]
            return new_w

            