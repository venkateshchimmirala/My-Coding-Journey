class Solution(object):
    def minSubArrayLen(self, target, nums):
        min = float('+inf')
        sum = l = r = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                if r - l + 1 < min:
                    min = r - l + 1
                sum -= nums[l]
                l += 1
            r += 1
        if min == float('inf'):
            return 0
        else:
            return min
