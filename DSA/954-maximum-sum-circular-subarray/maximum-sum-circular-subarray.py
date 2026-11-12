class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = sum(nums)
        maxx = float('-inf')
        min = float('inf')
        max_c = 0
        min_c = 0
        for i in nums:
            max_c += i
            if max_c > maxx:
                maxx = max_c
            if max_c < 0:
                max_c=0
        for i in nums:
            min_c += i
            if min_c < min:
                min = min_c
            if min_c > 0:
                min_c = 0
        if maxx < 0:
            return maxx
        return max(total_sum - min,maxx)
    
           
            