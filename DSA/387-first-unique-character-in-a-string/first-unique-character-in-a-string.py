class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in s:
            if d[i] == 1:
                return s.index(i)
        return -1

  