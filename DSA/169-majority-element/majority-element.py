class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i,j in d.items():
            if j > len(nums) / 2:
                return i