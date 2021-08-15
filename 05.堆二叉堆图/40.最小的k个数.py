"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 堆
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if k == 0:
#             return []
#         heap = arr[0:k]
#         for i in range(k // 2, -1, -1):
#             self.shift(i, k - 1, heap)
#         for j in range(k, len(arr)):
#             if arr[j] < heap[0]:
#                 heap[0] = arr[j]
#                 self.shift(0, k - 1, heap)
#             else:
#                 continue
#         return heap
#
#     def shift(self, left, right, arr):
#         tmp = arr[left]
#         j = 2 * left + 1
#         while j <= right:
#             if j + 1 <= right and arr[j + 1] > arr[j]:
#                 j += 1
#             if arr[j] > arr[left]:
#                 arr[left], arr[j] = arr[j], arr[left]
#                 left = j
#                 j = 2 * left + 1
#             else:
#                 break
#         arr[left] = tmp

import random


# 快排
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr
        res = self.quick_sort(arr, 0, len(arr) - 1, k)
        return res

    def quick_sort(self, arr, left, right, k):
        if left <= right:
            mid = self.partition(arr, left, right)
            if k < mid:
                return self.quick_sort(arr, left, mid - 1, k)
            elif k > mid:
                return self.quick_sort(arr, mid + 1, right, k)
            else:
                return arr[0:k]

    def partition(self, arr, left, right):
        pivot = random.randint(left, right)
        arr[left], arr[pivot] = arr[pivot], arr[left]
        tmp = arr[left]
        while left < right:
            # 如果左边的数大于tmp
            while left < right and arr[right] >= tmp:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= tmp:
                left += 1
            arr[right] = arr[left]
        arr[left] = tmp
        return left


arr = [0, 1, 1, 1, 4, 5, 3, 7, 7, 8, 10, 2, 7, 8, 0, 5, 2, 16, 12, 1, 19, 15, 5, 18, 2, 2, 22, 15, 8, 22, 17, 6, 22, 6,
       22, 26, 32, 8, 10, 11, 2, 26, 9, 12, 9, 7, 28, 33, 20, 7, 2, 17, 44, 3, 52, 27, 2, 23, 19, 56, 56, 58, 36, 31, 1,
       19, 19, 6, 65, 49, 27, 63, 29, 1, 69, 47, 56, 61, 40, 43, 10, 71, 60, 66, 42, 44, 10, 12, 83, 69, 73, 2, 65, 93,
       92, 47, 35, 39, 13, 75]
k = 75
res = Solution().getLeastNumbers(arr, k)
print(res)
