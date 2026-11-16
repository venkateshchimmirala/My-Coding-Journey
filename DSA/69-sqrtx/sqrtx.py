class Solution(object):
    def mySqrt(self, x):
        start = 0
        end = x
        while start <= end:
            mid = (start+end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
        return end
        