class Solution(object):
    def minEatingSpeed(self, piles, h):
        def caneat(piles, mid, h):
            hours = 0
            for i in piles:
                hours += (i + mid - 1) / mid
            return hours <= h

        start = 1
        end = max(piles)
        ens = end
        while start <= end:
            mid = (start+end)//2
            if caneat(piles, mid, h):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
                
        

        