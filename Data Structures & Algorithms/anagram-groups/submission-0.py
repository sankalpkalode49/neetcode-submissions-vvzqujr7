class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = [(sorted(strs[i]), i) for i in range(len(strs))]  # Store sorted chars with original indices
        op = []
        used = set()  # Track indices of strings already grouped
        
        for i in range(len(s)):
            if i in used:
                continue  # Skip if already grouped
            l = [strs[i]]  # Start group with strs[i]
            used.add(i)  # Mark strs[i] as used
            for k in range(len(s)):
                if k != i and k not in used and s[i][0] == s[k][0]:  # Compare sorted chars
                    l.append(strs[k])  # Add matching anagram
                    used.add(k)  # Mark as used
            op.append(l)  # Add group to output
        
        return op