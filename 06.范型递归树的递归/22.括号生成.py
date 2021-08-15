"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 左括号可以随时生成
# 左括号的个数大于右括号的个数

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        """
        :type n: int
        :rtype: List[str]
        """
        self.recursion(0, 0, n, "", res)
        return res

    def recursion(self, left, right, n, s, res):
        # 如果
        if left == n and right == n:
            res.append(s)
            return
        if left < n:
            self.recursion(left + 1, right, n, s + "(", res)
        if left > right:
            self.recursion(left, right + 1, n, s + ")", res)


res = Solution().generateParenthesis(1)
print(res)
