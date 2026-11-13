class Solution(object):
    def threeSum(self, nums):
        # result = []
        # nums.sort()
        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     start = i + 1
        #     end = len(nums) - 1
        #     while start < end:
        #         sum = nums[i] + nums[start] + nums[end]
        #         if sum == 0:
        #             result.append([nums[i], nums[start], nums[end]])
        #             while start < end and nums[start] == nums[start+1]:
        #                 start += 1
        #             while start < end and nums[end] == nums[end-1]:
        #                 end -= 1
        #             start += 1
        #             end -= 1
        #         elif sum < 0:
        #             start += 1
        #         else:
        #             end -= 1
        # return result      
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if (nums[i] + nums[start] + nums[end]) == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif (nums[i] + nums[start] + nums[end]) > 0:
                    end -= 1
                else:
                    start += 1 
        return result