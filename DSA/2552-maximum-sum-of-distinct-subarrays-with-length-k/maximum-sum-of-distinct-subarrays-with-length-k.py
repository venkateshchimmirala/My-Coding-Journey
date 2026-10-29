class Solution(object):
    def maximumSubarraySum(self, nums, k):
        d = {}
        l = r = m = s = 0
        while r < len(nums):
            s += nums[r]
            d[nums[r]] = d.get(nums[r],0) + 1
            if r - l + 1 ==k:
                if len(d) == k:
                    if s > m:
                        m = s
                s -= nums[l]
                d[nums[l]] =  d.get(nums[l]) - 1
                if d[nums[l]] == 0:
                    d.pop(nums[l])
                l += 1
            r += 1
        return m


        