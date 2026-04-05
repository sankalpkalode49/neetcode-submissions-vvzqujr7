class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the list. This is the maximum possible length of the prefix.
        shortest_str = min(strs, key=len)
        
        # Initialize the prefix string.
        prefix = ""
        
        # Iterate through each character of the shortest string.
        # This is our outer loop.
        for j in range(len(shortest_str)):
            # Get the current character from the shortest string.
            char_to_check = shortest_str[j]
            
            # Now, iterate through all the other strings in the list to check for a match.
            # This is our inner loop.
            for i in range(len(strs)):
                # If the character doesn't match, we've found the end of the common prefix.
                if strs[i][j] != char_to_check:
                    return prefix
            
            # If we get here, it means the character matched in all strings.
            # So, we can safely add it to our prefix.
            prefix += char_to_check
            
        # If the outer loop completes, the shortest string is the common prefix.
        return prefix