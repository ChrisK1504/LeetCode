class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        thisset = set()
        for i in nums:
            if i in thisset:
                return True
            thisset.add(i)
        return False