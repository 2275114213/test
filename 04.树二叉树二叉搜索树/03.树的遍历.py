class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.traverse_path = []

    def preorder(self, root):
        """
        根节点-》左子树-》右子树
        :param root:
        :return:
        """
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        """
        左子树-》根节点-》右子树
        :param root:
        :return:
        """
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        """
        左子树-》右子树-》根节点
        :param root:
        :return:
        """
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
