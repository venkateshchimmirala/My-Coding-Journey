class Solution(object):
    def pivotIndex(self, nums):
        ts = sum(nums)
        ls = 0
        for i in range(len(nums)):
            rs = ts - ls - nums[i]
            if rs == ls:
                return i
            ls += nums[i]
        return -1