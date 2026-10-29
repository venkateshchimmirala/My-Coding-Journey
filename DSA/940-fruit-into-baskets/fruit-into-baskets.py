class Solution(object):
    def totalFruit(self, fruits):
        l = r = m = 0
        d = {}
        while r < len(fruits):
            d[fruits[r]] = d.get(fruits[r],0) + 1
            while len(d) > 2:
                d[fruits[l]] = d.get(fruits[l]) - 1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l += 1
            m = max(m,r - l + 1)
            r += 1
        return m