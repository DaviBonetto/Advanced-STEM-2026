class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The output array does not count as extra space for analysis
        res = [1] * (len(nums))
        
        # Pass 1: Prefix products (Left -> Right)
        # Store prefix product directly in result array
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Suffix products (Right -> Left)
        # Multiply existing prefix result by suffix product on the fly
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
