class Solution(object):
    def containsDuplicate(self, nums):
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0) + 1
        # for i in nums:
        #     if d[i] > 1:
        #         return True
        # return False
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False
        