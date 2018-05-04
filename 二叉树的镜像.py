# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # 递归交换左右子树;理解二叉树的递归定义
        if root:
            root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
            return root
        else:
            return None