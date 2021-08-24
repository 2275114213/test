# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。 
# 
#  问总共有多少条不同的路径？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：m = 3, n = 7
# 输出：28 
# 
#  示例 2： 
# 
#  
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
#  
# 
#  示例 3： 
# 
#  
# 输入：m = 7, n = 3
# 输出：28
#  
# 
#  示例 4： 
# 
#  
# 输入：m = 3, n = 3
# 输出：6 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 100 
#  题目数据保证答案小于等于 2 * 109 
#  
#  Related Topics 数学 动态规划 组合数学 
#  👍 1086 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f[i][j]  表示从（i，j ）走到 end 多少中方法
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i][j + 1] + f[i + 1][j]
        return f[0][0]

    def uniquePaths3(self, m: int, n: int) -> int:
        # f[i][j]  表示从start 到（i，j) 的不同路径
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

    #  简单说就是压缩的维度是循环计算的历史。因为状态转移方程只跟前一行和前一列的相邻两个值有关，在循环嵌套里计算的时候，前一行的值就是上一个循环的计算结果，只需要考录列这一个维度就行了

    def uniquePaths1(self, m: int, n: int) -> int:
        # f[i][j]
        f = [1] * n
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    f[j] = 1
                else:
                    f[j] = f[j] + f[j + 1]
        return f[0]

    def uniquePaths2(self, m: int, n: int) -> int:
        # f[i][j]
        f = [1] * n
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    f[j] = 1
                else:
                    f[j] = f[j] + f[j - 1]
        return f[n - 1]
    # leetcode submit region end(Prohibit modification and deletion)


res = Solution().uniquePaths2(3, 2)
print(res)
