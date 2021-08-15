"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
        print(res)
        hashlist = [[key, v] for key, v in res.items()]
        print(hashlist)
        heap = hashlist[0:k]
        for i in range(k // 2, -1, -1):
            self.shift(i, k - 1, heap)
        for j in range(k, len(hashlist)):
            print(j)
            if hashlist[j][1] > heap[0][1]:
                heap[0] = hashlist[j]
                self.shift(0, k - 1, heap)

        for l in range(k):
            heap[0], heap[l] = heap[l], heap[0]
            self.shift(0, k - l - 1, heap)
        return [heap[i][0] for i in range(k)]

    def shift(self, left, right, arr):
        tmp = arr[left]
        j = 2 * left + 1
        while j <= right:
            if j + 1 <= right and arr[j + 1][1] < arr[j][1]:
                j = j + 1
            if arr[left][1] > arr[j][1]:
                arr[left], arr[j] = arr[j], arr[left]
                left = j
                j = 2 * left + 1
            else:
                break
        arr[left] = tmp


nums = [1, 1, 1, 2, 2, 3]
k = 2
res = Solution().topKFrequent(nums, k)
print(res)
