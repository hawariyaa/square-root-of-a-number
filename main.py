# this question asks us to find the square root of a number,
# if it is in decimal then round it down
# example x = 8  out-put = 2
# so here we could use brutforce going one by one but here we are going to use binary search
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2  # // interger division 3 // 2 = 1
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
            else:
                return m
        return r
x = 3
num = Solution()
answer = num.mySqrt(x)
print(answer)