class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
            if hashMap.get(target-nums[i], 0) != 0:
                return [i, hashMap.get(target-nums[i])]
            hashMap[nums[i]] = i
        return [0,0]