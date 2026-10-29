class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0    
        while l < r:
            d = r - l
            min_h = min(height[r], height[l])
            area = d * min_h

            if area > max_area:
                max_area = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area   