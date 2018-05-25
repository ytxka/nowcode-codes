# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # 先中序遍历，再把中序遍历结果组织成一个双向链表
        # 中序遍历结果中，每一个元素的right=下一个元素，下一个元素的left=上一个元素
        # 比如将二元查找树
        #                                     10
        #                                   /     \
        #                                 6       14
        #                               /   \    /   \
        #                              4     8   12  16
        # 转换成双向链表：4=6=8=10=12=14=16
        if not pRootOfTree:
            return None
        self.arr = []
        self.midTraverse(pRootOfTree)
        for index, item in enumerate(self.arr[:-1]):
            item.right = self.arr[index + 1]
            self.arr[index + 1].left = item
        return self.arr[0]
    
    def midTraverse(self, root):
        # 中序遍历二叉树，递归版
        if not root:
            return []
        self.midTraverse(root.left)
        self.arr.append(root)
        self.midTraverse(root.right)