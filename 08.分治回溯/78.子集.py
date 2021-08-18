"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            import copy
            da = copy.deepcopy(res)
            for num in da:
                if num:
                    num.append(i)
                    res.append(num)
            res.append([i])
        return res


nums = [1, 2, 3]
res = Solution().subsets(nums)
print(res)
print(len([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))
