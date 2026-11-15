class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        l=[]
        # a=set(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if d[i]>1:
                l.append(i)
        return l
