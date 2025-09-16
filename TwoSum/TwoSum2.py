class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return (seen[complement], i)
            seen[value] = i
        return None
                    
