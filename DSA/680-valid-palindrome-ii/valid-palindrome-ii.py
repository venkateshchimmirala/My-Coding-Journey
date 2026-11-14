class Solution(object):
    def validPalindrome(self, s):
        def is_validpalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (is_validpalindrome(left+1, right) or is_validpalindrome(left, right-1))
            left += 1
            right -= 1
        return True
        