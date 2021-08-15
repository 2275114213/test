"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root == None:
    #         return True
    #     res = []
    #
    #     def inorder(root, res):
    #         if root:
    #             inorder(root.left, res)
    #             res.append(root.val)
    #             inorder(root.right, res)
    #
    #     inorder(root, res)
    #     for i in range(len(res) - 1):
    #         if res[i] >= res[i + 1]:
    #             return False
    #     return True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        self.last = ""

        def inorder(root):
            if root:
                inorder(root.left)
                if root.val < self.last:
                    return False
                self.last = root.val
                inorder(root.right)
            else:
                return True

        res = inorder(root)
        return res
