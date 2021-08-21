"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],
 3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 中序遍历 递归
        # res = []
        #
        # def inorder(node, res):
        #     if node:
        #         inorder(node.left, res)
        #         res.append(node.val)
        #         inorder(node.right, res)
        #
        # inorder(root, res)
        # return res
        # 中序遍历 迭代
        # res, stk = [], []
        # while root or stk:
        #     while root:
        #         stk.append(root)
        #         root = root.left
        #     root = stk.pop()
        #     res.append(root.val)
        #     root = root.right
        # return res
        # bfs 模板
        """

        :param root:
        :return:
        if root == None:
            return
        queue = []
        ans = []
        queue.append(root)
        while queue:
            cnt = len(queue)
            tmp = []
            # 删除根节点
            node = queue.pop(0)
            ans.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return ans

        """
        # if root == None:
        #     return []
        # queue = []
        # ans = []
        # queue.append(root)
        # while queue:
        #     cnt = len(queue)
        #     tmp = []
        #     for _ in range(cnt):
        #         # 删除根节点
        #         node = queue.pop(0)
        #         if node.left != None:
        #             queue.append(node.left)
        #         if node.right != None:
        #             queue.append(node.right)
        #         tmp.append(node.val)
        #     ans.append(tmp)
        # return ans

        # 深度优先
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root:
            return res
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        for i in [root.left, root.right]:
            self.level(i, level + 1, res)


def list_to_binarytree(nums):
    def level(index):
        if index > len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


nums = [3, 9, 20, None, None, 15, 7]
node = list_to_binarytree(nums)
res = Solution().levelOrder(node)
print(res)
