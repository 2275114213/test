# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
#  示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics 数组 双指针 排序
#  👍 3671 👎 0

from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        current_dict = {}
        if not nums:
            return []
        if nums[0] > 0:
            return []
        left, right = 0, len(nums)
        for first in range(right - 2):
            target = -nums[first]
            for second in range(first + 1, right):
                third = target - nums[second]
                if third in current_dict:
                    if [nums[first], third, nums[second]] not in res:
                        res.append([nums[first], third, nums[second]])
                if nums[second] not in current_dict:
                    current_dict[nums[second]] = second
            current_dict = {}
        return res
        # leetcode submit region end(Prohibit modification and deletion)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis = []
        nums.sort()
        print(nums)
        for index, item in enumerate(nums[:-2]):
            j = index + 1
            k = len(nums) - 1
            if item > 0:
                break
            if index > 0 and item == nums[index - 1]:
                continue
            while j < k:
                if nums[j] + nums[k] < -item:
                    j += 1
                elif nums[j] + nums[k] > -item:
                    k -= 1
                else:
                    lis.append([nums[j], nums[k], item])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return lis


nums = [-1, 0, 0, 0, 0, 1, 1, 1]
res = Solution().threeSum(nums)
print(res)
