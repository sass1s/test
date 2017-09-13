import time


class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.

        sum_zeros = 0
        c = 1
        while n >= 5 ** c:
            count = n // 5 ** c
            sum_zeros += count
            c += 1
        return sum_zeros
        # import math
        # fac = math.factorial(n)
        # c = 0
        # while fac % 10 == 0:
        #     fac /= 10
        #     c += 1
        # if c == 0:
        #     return '末尾不含0'
        # else:
        #     return c


a = time.time()
print(Solution().trailingZeros(100))
print(time.time() - a)
