lst = [5, 2, 3, 1]

# 普通排序 （超时）
# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums) ):
#                 if nums[i] > nums[j]:
#                     nums[i], nums[j] = nums[j], nums[i]
#         return nums
#
#
# res = Solution().sortArray(lst)
# print(res)

# 冒泡排序 (超时)
# lst = [5, 2, 3, 1]
#
#
# class Solution(object):
#     def sortArray(self, nums):
#         """
#        :type nums: List[int]
#        :rtype: List[int]
#        """
#         exchange = False
#         for i in range(len(nums) - 1):
#             for j in range(0, len(nums) - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     nums[j + 1], nums[j] = nums[j], nums[j + 1]
#                     exchange = True
#             if not exchange:
#                 break
#         return nums
#
#
# res = Solution().sortArray(lst)
# print(res)


# 选择排序(超时)
# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             min_pos = i
#             for j in range(i + 1, len(nums)):
#                 if nums[j] < nums[min_pos]:
#                     min_pos = j
#             nums[i], nums[min_pos] = nums[min_pos], nums[i]
#         return nums
#
# lst = [-1,2,-8,-10]
# res = Solution().sortArray(lst)
# print(res)


# 插入排序
# class Solution(object):
#     def sortArray(self, nums):
#         for i in range(len(nums)):
#             tmp = nums[i]
#             j = i - 1
#             while j >= 0 and tmp < nums[j]:
#                 nums[j + 1], nums[j] = nums[j], nums[j + 1]
#                 j -= 1
#         return nums
# lst = [-1,2,-8,-10]
# res = Solution().sortArray(lst)
# print(res)

# 快速排序
import random

# class Solution:
#     def randomized_partition(self, nums, l, r):
#         # pivot = random.randint(l, r)
#         # nums[pivot], nums[r] = nums[r], nums[pivot]
#         i = l - 1
#         for j in range(l, r):
#             if nums[j] < nums[r]:
#                 i += 1
#                 nums[j], nums[i] = nums[i], nums[j]
#                 print("i", nums[i], nums[j], i, j)
#         i += 1
#         nums[i], nums[r] = nums[r], nums[i]
#         print("======", nums)
#         return i
#
#     def randomized_quicksort(self, nums, l, r):
#         if r - l <= 0:
#             return
#         mid = self.randomized_partition(nums, l, r)
#         print("mid",mid,nums)
#         self.randomized_quicksort(nums, l, mid - 1)
#         self.randomized_quicksort(nums, mid + 1, r)
#
#     def sortArray(self, nums):
#         self.randomized_quicksort(nums, 0, len(nums) - 1)
#         return nums
#
#
# lst = [-1, 2, -8, -10]
# # lst = [-10, 2, -8, -1]   # i = -1 j = 0   i = 0
# # lst = [-10, -8, 2, -1]   # i = 0  j = 2   i = 2
#
#
# # lst = [3, 4, 2, 1, 6, 5, 10, 7]
# res = Solution().sortArray(lst)
# print(res)

#
# class Solution:
#     def quick_sort(self, li, left, right):
#         if left < right:  # 待排序区至少有两个元素
#             mid = self.partition(li, left, right)
#             self.quick_sort(li, left, mid - 1)
#             self.quick_sort(li, mid + 1, right)
#
#     def partition(self, li, left, right):
#         pivot = random.randint(left, right)
#         li[pivot], li[left] = li[left], li[pivot]
#         tmp = li[left]
#         # 取出待排区的第一个元素, 然后将它归位
#         while left < right:
#             while left < right and li[right] >= tmp:
#                 right -= 1
#             li[left] = li[right]
#             while left < right and li[left] <= tmp:
#                 left += 1
#             li[right] = li[left]
#         li[left] = tmp
#         return left
#
#     def sortArray(self, nums):
#         self.quick_sort(nums, 0, len(nums) - 1)
#         return nums


# # 构造大根堆
# class Solution:
#     def sortArray(self, nums):
#         # 构造大根堆
#         n = len(nums)
#         for i in range(n // 2 - 1, -1, -1):
#             self.shift(nums, i, n - 1)
#         for hight in range(n-1,-1,-1):
#             nums[0], nums[hight] = nums[hight], nums[0]
#             self.shift(nums, 0,hight - 1)
#         return nums
#
#     def shift(self, nums, left, right):
#         tmp = nums[left]
#         j = 2 * left + 1
#         # 说明他有子节点
#         while j <= right:
#             # 如果存在右节点 且 左节点小于右节点
#             if j + 1 <= right and nums[j] < nums[j + 1]:
#                 j = j + 1
#             if nums[j] > tmp:
#                 nums[left] = nums[j]
#                 left = j
#                 j = 2 * left + 1
#             else:
#                 break
#         nums[left] = tmp


# 判断一个数字是否存在列表中
# lst1 = [1, 2, 3, 4]
# lst2 = [0 for i in range(len(lst) + 1)]
# for el in lst1:
#     lst2[el] = 1
# print(lst2[4] == 1)  # 时间查找复杂度是o(1), 没有什么比索引查找更快,但是占内存,


# 查询列表里面出现奇数次的那个数
# li = [1, 1, 2, 2, 3, 2, 3]
# a = 0
# for i in li:
#     a = a ^ i
# # // a^0 = a
# # // a^a = 0
# print(a)

# 需求不能用if while 关键字 写出具有if while 功能的语句
a = -1
s = "hello"
a > 0 and print(s)

#


import heapq

li = [9, 8, 7, 6, 5, 0, 1, 2, 4, 3]
res = heapq.nlargest(5, li)
print(res)
