class Solution(object):
    def maxSubArray(self, nums):
        c = 0
        max = float('-inf')
        for i in range(len(nums)):
            c += nums[i]
            if c > max:
                max = c
            if c < 0:
                c = 0
        return max
