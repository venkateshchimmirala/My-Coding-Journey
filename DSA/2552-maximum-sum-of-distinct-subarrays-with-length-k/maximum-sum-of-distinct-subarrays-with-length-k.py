class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = r = s = maxx = 0
        d = {}
        while r < len(nums):
            s += nums[r]
            d[nums[r]] = d.get(nums[r],0) + 1
            if r - l + 1 == k:
                if len(d) == k:
                    if s > maxx:
                        maxx = s
                s -= nums[l]
                d[nums[l]] = d.get(nums[l]) - 1
                if d[nums[l]] == 0:
                    d.pop(nums[l])
                l += 1
            r += 1
        return maxx


        