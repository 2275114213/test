"""
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = dict()
        for i in range(len(strs)):
            str = ''.join(sorted(strs[i]))
            if str not in res_dict:
                res_dict[str] = [strs[i]]
            else:
                res_dict[str].append(strs[i])
        return list(res_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = Solution().groupAnagrams(strs)
print(res)
