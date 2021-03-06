"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[j] < height[i]:
                he = height[j]
            else:
                he = height[i]
            max_area = max(max_area, (j - i) * he)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
area = Solution().maxArea(height)
print(area)
