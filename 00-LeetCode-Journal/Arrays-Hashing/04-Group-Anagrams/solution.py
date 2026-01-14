from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Mapping charCount to list of Anagrams
        ans = defaultdict(list)
        
        for s in strs:
            # Create a count array for a-z (26 characters)
            count = [0] * 26
            
            for c in s:
                # Map 'a' -> 0, 'b' -> 1... by using ASCII values
                count[ord(c) - ord('a')] += 1
            
            # Lists cannot be dict keys, so we convert to tuple
            ans[tuple(count)].append(s)
            
        return list(ans.values())
