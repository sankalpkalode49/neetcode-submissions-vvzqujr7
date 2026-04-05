class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # Create a hash map to store character counts for string s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement counts for characters in string t
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        # Check if all counts are zero (optional, but good practice)
        for count in char_count.values():
            if count != 0:
                return False

        return True
            

                
            