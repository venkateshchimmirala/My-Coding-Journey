class Solution(object):
    def findDuplicates(self, nums):
        # d={}
        # l=[]
        # a=set(nums)
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        # for i in a:
        #     if d[i]>1:
        #         l.append(i)
        # return l
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                result.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]

        return result
