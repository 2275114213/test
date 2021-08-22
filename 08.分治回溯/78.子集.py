"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List


# 循环
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            newsets = []
            print(res)
            for subset in res:
                new_sub = subset + [num]
                newsets.append(new_sub)
            res.extend(newsets)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            result.append([])
            return result

        def helper(result, nums, lis, index):
            if index == len(nums):
                result.append(lis)
                return
            helper(result, nums, lis, index + 1)
            lis.append(nums[index])
            helper(result, nums, lis, index + 1)
            red = lis.pop()

        helper(result, nums, [], 0)
        return result


nums = [1, 2, 3]
res = Solution().subsets(nums)
print(res)
print(len([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))
