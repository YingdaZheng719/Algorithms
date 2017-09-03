class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        res = x % 10
        x = x / 10
        while x > 0:
            res = res * 10 + x % 10
            x = x / 10
        if res*sign > 2**31-1 or res*sign < -2**31:
            return 0
        return res*sign
        