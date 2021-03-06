# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 位运算 数组 回溯 
#  👍 631 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return nums
        nums.sort()
        self.res = []

        def helper(index, lis, nums):
            if index == len(nums):
                self.res.append(lis.copy())
                return
                # 到下一层
            # if self.res and lis != self.res[-1]:
            if lis not in self.res:
                helper(index + 1, lis, nums)
            lis.append(nums[index])
            helper(index + 1, lis, nums)
            # 清理当前层
            lis.pop()

        helper(0, [], nums)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().subsetsWithDup([4,4,4,1,4])
print(res)
