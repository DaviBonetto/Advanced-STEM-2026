class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
