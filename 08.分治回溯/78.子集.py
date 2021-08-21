"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List


# 循环
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for num in nums:
#             newsets = []
#             print(res)
#             for subset in res:
#                 new_sub = subset + [num]
#                 newsets.append(new_sub)
#             res.extend(newsets)
#         return res


# 递归里面套循环： 记住递归结束继续循环

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        if not nums:
            self.result.append([])
            return self.result

        def helper(nums, lis, index):
            if index == len(nums):
                self.result.append(lis.copy())
                return
            helper(nums, lis, index + 1)

            lis.append(nums[index])
            helper(nums, lis, index + 1)
            lis.pop()

        helper(nums, [], 0)
        return self.result


nums = [1, 2, 3]
res = Solution().subsets(nums)
print(res)
