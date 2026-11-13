class Solution(object):
    def maxArea(self, height):
        max_amount = float('-inf')
        left = 0
        right = len(height) - 1
        while left < right:
            min_height = min(height[left], height[right])
            w = right - left
            area = min_height * w
            max_amount = max(area,max_amount)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_amount
