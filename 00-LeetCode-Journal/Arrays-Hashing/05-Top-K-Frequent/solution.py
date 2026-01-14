class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        # Frequency bucket: index = count, value = list of numbers
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Count frequency of each number
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Place numbers into buckets based on frequency
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        # Iterate backwards from highest frequency (len(nums)) to 1
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
