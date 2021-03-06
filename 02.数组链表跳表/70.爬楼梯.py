"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     f1, f2, f3 = 1, 2, 3
    #     for i in range(3, n + 1):
    #         f3 = f1 + f2
    #         f1 = f2
    #         f2 = f3
    #     return f3

    def climbStairs(self, n: int) -> list:
        a = list()
        if n == 0:
            return a
        a.extend([0, 1])
        for i in range(2, n):
            tmp = a[i - 1] + a[i - 2]
            a.append(tmp)
        return a


res = Solution().climbStairs(8)
print(res)
