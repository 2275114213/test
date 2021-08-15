# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                if left!=right:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


nums = [0, 1, 0, 3, 12]
res = Solution().moveZeroes(nums)
print(nums)
