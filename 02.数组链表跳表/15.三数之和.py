"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for first in range(len(nums) - 2):
            nums.sort()
            target = -nums[first]
            left, right = first + 1, len(nums) - 1
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[left] > target:
                continue
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[first], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < target:
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    left += 1
                else:
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    right -= 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(nums)
print(res)
"""
Linked List 实战题目
反转链表（字节跳动、亚马逊在半年内面试常考）
两两交换链表中的节点（阿里巴巴、字节跳动在半年内面试常考）
环形链表（阿里巴巴、字节跳动、腾讯在半年内面试常考）
环形链表 II
 K 个一组翻转链表（字节跳动、猿辅导在半年内面试常考）
xing
"""