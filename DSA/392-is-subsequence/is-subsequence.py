class Solution(object):
    def isSubsequence(self, s, t):
        si = 0
        ti = 0
        while si < len(s):
            while ti < len(t):
                if s[si] == t[ti]:
                    ti += 1
                    break
                ti += 1
            else:
                return False
            si += 1
        return True

        