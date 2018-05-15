# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 理解了根据前序遍历、中序遍历结果重建二叉树的方法后，利用递归编写函数即可
        if not pre or not tin:
            return None
        else:
            root = TreeNode(pre.pop(0))
            index = tin.index(root.val)
            root.left = self.reConstructBinaryTree(pre, tin[:index])
            root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
            return root