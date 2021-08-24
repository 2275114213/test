# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  Related Topics 数组 回溯 
#  👍 668 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        if n == 0:
            return []

        def dfs(lis, index, n, k):
            if len(lis) == k:
                self.res.append(lis.copy())
                return
            if index == n + 1:
                return
            dfs(lis, index + 1, n, k)
            lis.append(index)
            dfs(lis, index + 1, n, k)
            lis.pop()

        dfs([], 1, n, k)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().combine(4, 2)
print(res)
