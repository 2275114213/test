# 循环
# class Solution(object):
#     def myPow(self, x, n):
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
#         if x == 0.0: return 0.0
#         if x == 1.0: return 1.0
#         res = 1
#         if n < 0:
#             x, n = 1 / x, -n
#         while n:
#             if n & 1:
#                 res *= x
#             x *= x
#             n >>= 1
#         return res

# 递归
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1 or x == 1.0:
            return x
        if n < 0:
            print(n)
            n = -n
            x = 1 / x
        return self.fastpow(x, n)

    def fastpow(self, x, n):
        if n == 0:
            return 1
        half = self.fastpow(x, n >> 1)  # n >> 1 ==    n // 2  取最大整数
        return half * half if not n & 1 else x * half * half  # n & 1 == n%2  如果为1的化说明有余数


res = Solution().myPow(2.000000, -2)
print(res)
