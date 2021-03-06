# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res = []
        self.MidSearch(pRoot)
        if 0 < k <= len(self.res):
            return self.res[k - 1]
        else:
            return None
    def MidSearch(self, root):
        if not root:
            return
        self.MidSearch(root.left)
        self.res.append(root)
        self.MidSearch(root.right)
