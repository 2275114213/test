"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。

 

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    # def myPow(self, x, n):
    #     """
    #     :type x: float
    #     :type n: int
    #     :rtype: float
    #     """
    #     if x == 0.0: return 0.0
    #     if x == 1.0: return 1.0
    #     res = 1
    #     if n < 0:
    #         x, n = 1 / x, -n
    #     while n:
    #         if n & 1:
    #             res *= x
    #         x *= x
    #         n >>= 1
    #     return res
    def myPow(self, x, n):
        if n < 0:
            x = x / 1
            n = -n
        print("n",n)
        return self.fastpow(x, n)

    def fastpow(self, x, n):
        print(n)
        if n == 0:
            return 1.0
        half = self.fastpow(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x


res = Solution().myPow(2.00000, 10)
print(res)
