class Solution(object):
    def findDuplicates(self, nums):
        d={}
        l=[]
        a=set(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]>1:
                l.append(i)
        return l
