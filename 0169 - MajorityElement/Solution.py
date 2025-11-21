class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        majority = nums[0]
        for num in nums:
            majority = num if count==0 else majority
            count += 1 if majority != num else -1
        
        return majority