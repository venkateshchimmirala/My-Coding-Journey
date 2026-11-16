class Solution(object):
    def searchRange(self, nums, target):
        def firstpostion():
            start = 0
            end = len(nums) - 1
            index = -1
            while start <= end:
                mid = (start + end ) // 2
                if nums[mid] == target:
                    index = mid
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid -1 
            return index
        def lastpostion():
            index = -1
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    index = mid
                    start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end= mid - 1
            return index
        return [firstpostion(),lastpostion()]
        