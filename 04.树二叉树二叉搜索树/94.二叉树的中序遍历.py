"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
root = [1,null,2,3]
"""
from typing import List


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # def inorder(root, res):
        #     if root:
        #         inorder(root.left, res)
        #         res.append(root.val)
        #         inorder(root.right, res)
        #     else:
        #         return
        #
        # res = []
        # inorder(root, res)
        # return res

        # 迭代方式
        res, stk = [], []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root, res):
            if root:
                res.append(root.val)
                preorder(root.left, res)
                preorder(root.right, res)

        res = []
        preorder(root, res)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def posorder(root, res):
            if root:
                posorder(root.left, res)
                posorder(root.right, res)
                res.append(root.val)

        res = []
        posorder(root, res)
        return res


def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


binary_tree = list_to_binarytree([1, None, 2, None, None, 3])
print(binary_tree.left)
inorder = Solution().inorderTraversal(binary_tree)
print(inorder)
preorder = Solution().preorderTraversal(binary_tree)
print(preorder)
