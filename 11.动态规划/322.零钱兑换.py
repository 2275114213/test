# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 
# 
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：coins = [1], amount = 1
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：coins = [1], amount = 2
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 广度优先搜索 数组 动态规划 
#  👍 1436 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1



# leetcode submit region end(Prohibit modification and deletion)
"""
比较典型的动态规划问题。

假设 f(n) 代表要凑齐金额为 n 所要用的最少硬币数量，那么有：

f(n) = min(f(n - c1), f(n - c2), ... f(n - cn)) + 1
其中 c1 ~ cn 为硬币的所有面额。

----

再具体解释一下这个公式吧，例如这个示例：

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
题目求的值为 f(11)，第一次选择硬币时我们有三种选择。

假设我们取面额为 1 的硬币，那么接下来需要凑齐的总金额变为 11 - 1 = 10，即 f(11) = f(10) + 1，这里的 +1 就是我们取出的面额为 1 的硬币。

同理，如果取面额为 2 或面额为 5 的硬币可以得到：

f(11) = f(9) + 1
f(11) = f(6) + 1
所以：

f(11) = min(f(10), f(9), f(6)) + 1
"""