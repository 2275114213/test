"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""


class Solution(object):
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        res = []
        if digits == "":
            return []
        self.recursion("", digits, 0, res)
        return res

    def recursion(self, s, digits, i, res):
        """
        :param s:
        :param digits: 整个输入的参数
        :param i:  level
        :param res:
        :param map:
        :return:
        """
        # terminator
        if i == len(digits):
            res.append(s)
            return
        # process
        letters = self.phoneMap.get(digits[i])
        print(letters)
        for j in range(len(letters)):
            self.recursion(s + letters[j], digits, i + 1, res)


res = Solution().letterCombinations("23")
print(res)
