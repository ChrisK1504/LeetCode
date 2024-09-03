class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        
        hashset = set()
        for i in nums:
            hashset.add(i)

        max_length = 0
        for i in hashset:
            if i-1 not in hashset:
                temp_length = 1
                while i+1 in hashset:  
                    temp_length += 1
                    i += 1
                max_length = max(max_length, temp_length)
        return max_length
        