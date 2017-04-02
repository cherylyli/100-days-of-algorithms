class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = False
                
        for key in seen.keys():
            return key