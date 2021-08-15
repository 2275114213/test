"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在··滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

import heapq

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         print(k)
#         q = [(-nums[i], i) for i in range(k)]
#         print(q)
#         # heapq 默认小根堆
#         heapq.heapify(q)
#         ans = [-q[0][0]]
#         for i in range(k, n):
#             # 判断堆顶元素（下标）是否在滑动窗口内
#             print(q[0][1])
#             while q and q[0][1] <= i - k:
#                 heapq.heappop(q)
#             # 把最新的元素加入大根堆
#             heapq.heappush(q, (-nums[i], i))
#             # 把大根堆的堆顶元素加入ans
#             ans.append(-q[0][0])
#         return ans

"""
维护窗口，向右移动时左侧超出窗口的值弹出，因为需要的是窗口内的最大值，所以只要保证窗口内的值是递减的即可，
小于新加入的值全部弹出。最左端即为窗口最大值 python解法：
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win, ret = [], []
        for i, v in enumerate(nums):
            # i 索引 v 值，如果最大值不再窗口了删除
            if i >= k and win[0] <= i - k:
                win.pop(0)
            # 如果新添加的值大于原来的值，将原来的值弹出
            while win and nums[win[-1]] <= v:
                win.pop()
            win.append(i)
            if i >= k - 1:
                ret.append(nums[win[0]])
        return ret


nums = [1, -1]
k = 1
res = Solution().maxSlidingWindow(nums, k)
print(res)
